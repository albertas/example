from typing import Optional


class CoolNewFeature:
    ...


class UnusedClass:
    this_class_is_not_used = True

    def but_we_will_have_to_maintain_it(self) -> Optional[bool]:
        return True

    def until_human_understands_that_its_not_used(self) -> str:
        return "But why not by static checker?"
