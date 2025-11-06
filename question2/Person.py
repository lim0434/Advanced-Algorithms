class Person:
    def __init__(self, name, biography, gender, privacy="public"): # MODIFIED: Added 'gender'
        self.name = name
        self.biography = biography
        self.gender = gender
        self.privacy = privacy

    def get_name(self):
        return self.name