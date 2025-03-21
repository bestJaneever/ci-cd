from robot.api.deco import library, keyword


@library(scope='GLOBAL', auto_keywords=True)
class Helper:
    @keyword
    def is_element_is_unique(self, collection, index) -> bool:
        value = collection[index]

        for i in range(0, len(collection)):
            if i == index:
                continue
            if collection[i][0] == value[0]:
                return False

        return True
