import requests
from hashlib import sha256
import json

class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []

    def add_block(self, sender, recipient, amount):
        block = {
            'index': len(self.chain) + 1,
            'transactions': self.transactions,
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender, recipient, amount):
        self.transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

    def mine_block(self, miner):
        previous_block = self.chain[-1]
        proof = 1
        while not self.valid_proof(previous_block['proof'], proof):
            proof += 1
        block = self.add_block(sender="0", recipient=miner, amount=1)
        block['proof'] = proof
        return block

    def valid_proof(self, last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

class UPIPayment:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def initiate_payment(self, sender, recipient, amount):
        # Perform UPI payment API call here
        # This is a placeholder, you need to replace it with actual UPI API calls
        upi_payment_response = self.perform_upi_payment(sender, recipient, amount)

        if upi_payment_response['success']:
            # If UPI payment is successful, add the transaction to the blockchain
            self.blockchain.add_transaction(sender, recipient, amount)
            return "UPI payment successful, transaction added to blockchain"
        else:
            return "UPI payment failed"

    def perform_upi_payment(self, sender, recipient, amount):
        # Placeholder UPI payment API call
        # Replace this with actual UPI payment API integration
        # This is just an example, and you need to replace it with a real UPI API
        return {'success': True, 'transaction_id': '1234567890'}

# Example usage
blockchain = Blockchain()
upi_payment = UPIPayment(blockchain)

# Initiate a UPI payment and add the transaction to the blockchain
result = upi_payment.initiate_payment(sender="sender_account", recipient="recipient_account", amount=10)
print(result)

# Mine a block to include the UPI transaction in the blockchain
mined_block = blockchain.mine_block(miner="miner_account")
print("Block mined:", mined_block)
