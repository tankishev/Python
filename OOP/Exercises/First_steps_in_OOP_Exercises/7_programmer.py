# Create a class called Programmer. Upon initialization it should receive name (string), language (string),
# skills (integer). The class should have two methods:
# -	watch_course(course_name, language, skills_earned)
# o	If the programmer's language is the same as the one on the course, increase his skills with the given amount
# and return a message "{name} watched {course_name}".
# o	Otherwise return "{name} does not know {language}".
# -	change_language(new_language, skills_needed)
# o	If the programmer has the skills and the new language is not the same as his, change his language to the new one
# and return "{name} switched from {previous_language} to {new_language}".
# o	If the programmer has the skills, but the given language is equal to his return "{name} already knows {language}".
# o	In the last case the programmer does not have the skills, so return "{name} needs {needed_skills} more skills"
# and do not change his language

class Programmer:

    def __init__(self, name: str, language: str, skills: int) -> None:
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name: str, language: str, skills_earned: int) -> str:
        if language == self.language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"

    def change_language(self, new_language: str, skills_needed: int) -> str:
        if self.skills >= skills_needed and new_language != self.language:
            prev_language = self.language
            self.language = new_language
            return f"{self.name} switched from {prev_language} to {new_language}"
        elif self.skills >= skills_needed and new_language == self.language:
            return f"{self.name} already knows {new_language}"
        elif self.skills < skills_needed:
            needed_skills = skills_needed - self.skills
            return f'{self.name} needs {needed_skills} more skills'
