from puzzle import BasePuzzle
import re

class IntValidator:
    def __init__(self, min_value, max_value):
        self.min = min_value
        self.max = max_value

    def validate(self, value):
        try:
            value = int(value)
            return value >= self.min and value <= self.max
        except:
            return False

class HeightValidator:
    def __init__(self):
        self.expression = re.compile("([0-9]+)(cm|in)")

    def validate(self, value):
        match = self.expression.fullmatch(value)

        if match:
            groups = match.groups()
            height = int(groups[0])
            unit = groups[1]

            if unit == "cm":
                return height >= 150 and height <= 193
            if unit == "in":
                return height >= 59 and height <= 76

        return False

class RegexValidator:
    def __init__(self, pattern):
        self.expression = re.compile(pattern)

    def validate(self, value):
        return self.expression.fullmatch(value)

class Passport:
    required_fields = {
        "byr": IntValidator(1920, 2002),
        "iyr": IntValidator(2010, 2020),
        "eyr": IntValidator(2020, 2030),
        "hgt": HeightValidator(),
        "hcl": RegexValidator("#[a-f0-9]{6}"),
        "ecl": RegexValidator("amb|blu|brn|gry|grn|hzl|oth"),
        "pid": RegexValidator("[0-9]{9}")
    }
    optional_fields = ["cid"]

    def __init__(self, fields):
        self.fields = fields

    def valid(self):
        fields = self.fields.copy()

        # Ensure required fields are set and valid
        for key, validator in self.required_fields.items():
            value = fields.pop(key, None)
            if not value or not validator.validate(value):
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
