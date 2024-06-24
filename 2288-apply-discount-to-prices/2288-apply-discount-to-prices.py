class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        tokens = sentence.split()
        discount /= 100

        for i, token in enumerate(tokens):
            # Check if it's in correct format
            price = token[1:]
            if token[0] == "$" and price.isdigit():
                discounted_price = int(price) * (1 - discount)
                formatted_price = "$" + "{:.2f}".format(discounted_price)

                tokens[i] = formatted_price

        return " ".join(tokens)  # Combine the updated list
