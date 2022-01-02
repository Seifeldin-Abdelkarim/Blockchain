import hashlib


class Block:  # the class of a block
    def __init__(
        self, details, pre_hash
    ):  # the details entered, pre_hash is the previous hash
        self.hash = hashlib.sha256()  # placing hashlib.sha256 in a variable called hash
        self.pre_hash = pre_hash
        self.nonce = 0  # nonce is the number added to the block to reach the criteria of the required block when hashing
        self.details = details

    def mine_block(
        self, limit
    ):  # limit is the requirment we set for any new added blocks
        self.hash.update(str(self).encode())
        while int(self.hash.hexdigest(), 16) > 2 ** (
            256 - limit
        ):  # the condition we need to mine the block
            self.nonce += 1  # nonce is increased everytime and hashed till we reach the hash we need
            self.hash = hashlib.sha256()
            self.hash.update(
                str(self).encode("utf-8")
            )  # the hash is updated everytime using hash.update

    def __str__(self):
        return "{}{}{}".format(
            self.pre_hash.hexdigest(), self.details, self.nonce
        )  # to print the previous hash, the details and the nonce
