def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    """
    Convert cat and dog ages to human years.

    Rules:
    Cat: first 15 years = 1 human year, next 9 = +1, then every 4 = +1
    Dog: first 15 years = 1 human year, next 9 = +1, then every 5 = +1
    """

    def cat_to_human(age: int) -> int:
        if age < 15:
            return 0
        human = 1
        age -= 15
        if age >= 9:
            human += 1
            age -= 9
        else:
            return human
        human += age // 4
        return human

    def dog_to_human(age: int) -> int:
        if age < 15:
            return 0
        human = 1
        age -= 15
        if age >= 9:
            human += 1
            age -= 9
        else:
            return human
        human += age // 5
        return human

    return [cat_to_human(cat_age), dog_to_human(dog_age)]