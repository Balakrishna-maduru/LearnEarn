expence_tracker = {"a": {"b": 0, "c": 0},
                   "b": {"a": 0, "c": 0},
                   "c": {"a": 0, "b": 0}
                   }


def spend(payer, members, amount_spend):
    split_amount = amount_spend/(len(members) + 1)
    for member in members:
        previous_balance = expence_tracker[member][payer]
        expence_tracker[member][payer] = previous_balance + split_amount
    aggegate(payer, members)


def aggegate(payer, members):
    e_payer = expence_tracker[payer]
    for member in members:
        for mem, m_value in expence_tracker[member].items():
            if mem in e_payer:
                if m_value >= e_payer[mem]:
                    expence_tracker[member][mem] = m_value + e_payer[mem]
                    e_payer[mem] = e_payer[mem] - m_value
                    expence_tracker[member][payer] = expence_tracker[member][payer] - m_value
            else:
                if e_payer[member] < expence_tracker[member][payer]:
                    expence_tracker[member][payer] = expence_tracker[member][payer] - \
                        e_payer[member]
                    e_payer[member] = 0
                else:
                    expence_tracker[member][payer] = e_payer[member] - \
                        expence_tracker[member][payer]

                    e_payer[member] = e_payer[member] - \
                        expence_tracker[member][payer]

                print(expence_tracker[member])


spend("a", ["b", "c"], 3000)
print("Transaction 1")
spend("b", ["c"], 3000)
print("Transaction 1")
spend("c", ["b"], 1000)
spend("a", ["b", "c"], 3000)

print(expence_tracker)
#{'a': {'b': 0, 'c': 0}, 'b': {'a': 1000.0, 'c': 0}, 'c': {'a': 1000.0, 'b': 1500.0}}
#{'a': {'b': 0, 'c': 0}, 'b': {'a': 0, 'c': 0}, 'c': {'a': 2000.0, 'b': 500.0}}
