from puzzle import BasePuzzle

class Passport:
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    optional_fields = ["cid"]

    def __init__(self, fields):
        self.fields = fields

    def valid(self):
        fields = self.fields.copy()

        # Ensure required fields are set
        for key in self.required_fields:
            if not fields.pop(key, None):
                return False

        # Ignore optional fields
        for key in self.optional_fields:
            fields.pop(key, None)

        # Ensure no other fields set
        return len(fields) == 0

class PassportReader:
    def read(self, lines):
        passports = []
        fields = {}

        for line in lines:
            if len(line) == 0:
                passports.append(Passport(fields))
                fields = {}
                continue

            tokens = line.split(" ")

            for token in tokens:
                key, value = token.split(":")

                fields[key] = value

        if fields:
            passports.append(Passport(fields))

        return passports

class Puzzle(BasePuzzle):
    def solve(self):
        passports = PassportReader().read(self.lines)
        valid_passports = [ passport for passport in passports if passport.valid() ]

        print("Valid passports: {}".format(len(valid_passports)))

if __name__ == "__main__":
    Puzzle().solve()
