#!/usr/bin/env python3

# Created By: Amara Tie

# Date: March 26, 2025

# This program calculates the total using subtotals and HST
import constants


def main():
    # The user enters the subtotal
    subtotal = float(input("Enter the subtotal: $"))

    # Calculate the tax and the total
    tax = subtotal * constants.TAX_RATE_ONTARIO / 100
    total = subtotal + tax

    # Display the total tax
    print("")
    print("The subtotal is ${:.2f}".format(subtotal))
    print("The HST is ${0:.2f} and the total would be ${1:.2f}".format(tax, total))


if __name__ == "__main__":
    main()
