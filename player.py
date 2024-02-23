class PlayerCharacter:
    def __init__(self, name, level, race, char_class, background, strength, 
                dexterity, constitution, intelligence, wisdom, charisma, 
                fey_ancestry, darkvision, eldritch_invocations, pact_of_the_tome, 
                skills, spellcasting_ability, spell_attack_bonus, spell_save_dc):
        # Basic attributes
        self.name = name
        self.level = level
        self.race = race
        self.char_class = char_class
        self.background = background

        # Ability scores and modifiers
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

        # Racial Traits and Warlock Abilities
        self.fey_ancestry = fey_ancestry
        self.darkvision = darkvision
        self.eldritch_invocations = eldritch_invocations
        self.pact_of_the_tome = pact_of_the_tome

        # Other character details
        self.skills = skills
        self.spellcasting_ability = spellcasting_ability
        self.spell_attack_bonus = spell_attack_bonus
        self.spell_save_dc = spell_save_dc

    def __str__(self):
        return f'''Name: {self.name}, Level: {self.level}, Race: {self.race}, Class: {self.char_class}, 
        Background: {self.background}, Strength: {self.strength}, Dexterity: {self.dexterity}, 
        Constitution: {self.constitution}, Intelligence: {self.intelligence}, Wisdom: {self.wisdom}, 
        Charisma: {self.charisma}, Fey Ancestry: {self.fey_ancestry}, Darkvision: {self.darkvision}, 
        Eldritch Invocations: {self.eldritch_invocations}, Pact of the Tome: {self.pact_of_the_tome}, 
        Skills: {self.skills}, Spellcasting Ability: {self.spellcasting_ability}, 
        Spell Attack Bonus: {self.spell_attack_bonus}, Spell Save DC: {self.spell_save_dc}'''

# Creating an instance of the character
nova_rift = PlayerCharacter("Nova Rift", 5, "Half-Elf", "Warlock", "Noble", 10, 15, 12, 13, 9, 17, True, True, 
                            ["Devil's Sight", "Awakened Insight", "Captured Heart"], True, 
                            {"Acrobatics": 2, "Arcana": 4, "Stealth": 5}, "Charisma", 3, 11)