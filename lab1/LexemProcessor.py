class LexemProcessor:
    main_string = ""

    @staticmethod
    def process_file(path: str):
        with open(path, 'r', encoding='utf-8') as file:
            main_string = file.read()
        return main_string
