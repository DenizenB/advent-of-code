from puzzle import BasePuzzle
from re import compile
import numpy as np


class TicketField:
    rule_expr = compile("([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)")

    def __init__(self, rule):
        groups = self.rule_expr.fullmatch(rule).groups()
        self.name = groups[0]

        self.ranges = []
        for i in range(1, len(groups), 2):
            min_value = int(groups[i])
            max_value = int(groups[i+1])
            self.ranges.append((min_value, max_value))

    def validate(self, value):
        for min_value, max_value in self.ranges:
            if value >= min_value and value <= max_value:
                return 0

        return value


class Ticket:
    def __init__(self, ticket_str):
        self.values = [int(value) for value in ticket_str.split(',')]


class TicketValidator:
    def __init__(self, fields):
        self.fields = fields
        self.positions = {}

    def errors(self, ticket):
        errors = 0

        for value in ticket.values:
            errors += min(map(lambda field: field.validate(value), self.fields))

        return errors

    def guess_positions(self, ticket):
        for field in self.fields:
            field_errors = map(lambda value: field.validate(value), ticket.values)
            valid_indexes = set([index
                    for (index, error) in enumerate(field_errors) if error == 0])

            if field in self.positions:
                self.positions[field].intersection_update(valid_indexes)
            else:
                self.positions[field] = valid_indexes

    def resolve_positions(self):
        # Sort by number of possible positions, fewest first
        sorted_fields = sorted(self.fields, key=lambda f: len(self.positions[f]))

        while len(sorted_fields) != 0:
            resolved_field = sorted_fields.pop(0)

            positions = self.positions[resolved_field]
            position = positions.pop()

            if len(positions) != 0:
                raise RuntimeError("More than 1 possible position")

            self.positions[resolved_field] = position

            for field in sorted_fields:
                self.positions[field].remove(position)


class Puzzle(BasePuzzle):
    def solve(self):
        sections = [section.splitlines() for section in self.input.split("\n\n")]
        fields, my_ticket, nearby_tickets = sections

        # Remove headers
        my_ticket.pop(0)
        nearby_tickets.pop(0)

        fields = [TicketField(field) for field in fields]
        validator = TicketValidator(fields)

        my_ticket = Ticket(my_ticket[0])

        nearby_tickets = [Ticket(ticket) for ticket in nearby_tickets]

        # Part one

        error_rate = sum(map(lambda t: validator.errors(t), nearby_tickets))
        print(f"Ticket error rate: {error_rate}")

        # Part two

        valid_tickets = list(filter(lambda t: validator.errors(t) == 0, nearby_tickets))

        for ticket in valid_tickets:
            validator.guess_positions(ticket)

        validator.resolve_positions()

        departure_fields = filter(lambda field: "departure" in field.name, fields)
        departure_indexes = map(lambda field: validator.positions[field], departure_fields)
        departure_values = map(lambda field: my_ticket.values[field], departure_indexes)
        product = np.prod(list(departure_values))

        print(f"Departure product: {product}")


if __name__ == "__main__":
    Puzzle().solve()
