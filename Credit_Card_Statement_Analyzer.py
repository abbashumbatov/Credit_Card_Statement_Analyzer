credit_card = {
    'Name':'Abbas',
    'Months':['Jan','Feb','Mar','Apr','May'],

    'Spendings':[
        {'Food':200,'Travel':50,'Shopping':150,'Bills':120},
        {"Food": 180, "Travel": 30, "Shopping": 80, "Bills": 130},
        {"Food": 250, "Travel": 100, "Shopping": 200, "Bills": 140},
        {"Food": 300, "Travel": 20, "Shopping": 90, "Bills": 110},
        {"Food": 150, "Travel": 80, "Shopping": 250, "Bills": 130}
    ],

    'Credit Limit':1500

}


def card_report(data):
    months = data['Months']
    spendings = data['Spendings']

    name = data['Name']
    credit_limit = data['Credit Limit']

    for i in range(len(months)):
        month_name = months[i]
        month_spending = spendings[i]

        total_spending = sum(month_spending.values())
        ratio = total_spending / credit_limit

        # Classification
        if ratio > 0.70:
            print('High Spending')
        elif ratio > 0.40:
            print('Moderate Spending')
        else:
            print('Low Spending')

        # WARNING COLLECTION LIST
        warnings = []

        # Warnings
        if any(amount > 250 for amount in month_spending.values()):
            warnings.append('Large Category Spend detected')

        food = month_spending['Food']
        shopping = month_spending['Shopping']
        bills = month_spending['Bills']

        if food > shopping:
            warnings.append('High Food Priority')

        if shopping > food:
            warnings.append('Impulsive shopping behaviour')

        if bills > 200:
            warnings.append('High fixed cost')

        # REPORT PRINT
        print(f'\n--- Report for month {months[i]} ---')
        print(f'Total Spending: {total_spending}')
        print(f"Status Ratio: {ratio:.2f}")

        print("Warnings:")
        if warnings:
            for w in warnings:
                print("-", w)
        else:
            print("None")

        print()  # extra line for readability


card_report(credit_card)
