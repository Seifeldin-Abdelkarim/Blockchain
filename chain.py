import hashlib
from block import Block


class Chain:  # the class of the chain that links the blocks together
    def __init__(self, limit):
        self.limit = limit
        self.list_blocks = []  # this contains the list of blocks added to the chain
        self.current_details = (
            []
        )  # this contains the current details added to the chain
        self.first_block()  # this calls the first_block function to make the initial block in the chain

    def add_block(
        self, block
    ):  # for adding the block in the list of blocks if the proof_of_work function agrees on the block
        if self.proof(block):
            self.list_blocks.append(block)

    def add_to_current_details(
        self, data
    ):  # appends the current details in the current_details list
        self.current_details.append(data)

    def first_block(self):  # initializing the first block
        h = hashlib.sha256()
        h.update("".encode("utf-8"))
        FirstBlock = Block("Start", h)  # hashes the word "Start" as the first block
        FirstBlock.mine_block(self.limit)  # mines the block
        self.list_blocks.append(
            FirstBlock
        )  # enters the first block into the list of blocks

    def proof(
        self, block
    ):  # proof that the block entered is the one we need and not just any random block
        hash = hashlib.sha256()
        hash.update(str(block).encode("utf-8"))
        return (  # returns the values only if the conditions of the block are correct which protects the validity of the blocks
            block.hash.hexdigest() == hash.hexdigest()
            and int(hash.hexdigest(), 16) < 2 ** (256 - self.limit)
            and block.pre_hash == self.list_blocks[-1].hash
            # that the previous hash is the same as the last hash in the list of blocks
        )

    def mine(self):
        if (
            len(self.current_details) > 0
        ):  # if there are details in the current_details list
            details = (
                self.current_details.pop()
            )  # adds current details to variable called details and pops the details from the list
            block = Block(
                details, self.list_blocks[-1].hash
            )  # the details and the previous hash
            block.mine_block(
                self.limit
            )  # mining the block with the requirment we set in the main.py file
            self.add_block(
                block
            )  # adding the block while verifying with the proof_of_work function

            slashes = "\n\n==================="  # placing all the printed text in variables that are going to be used in main.py file
            Hashinfo = ("Hash: ", block.hash.hexdigest())
            PreHashinfo = ("Previous Hash:", block.pre_hash.hexdigest())
            Nonceinfo = ("Nonce:", block.nonce)
            Details = ("Details:", block.details)
            print(slashes)
            print(Hashinfo)
            print(PreHashinfo)
            print(Nonceinfo)
            print(Details)
            return slashes, Hashinfo, PreHashinfo, Nonceinfo, Details
