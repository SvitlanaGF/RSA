class WorkWithFiles:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_txt(self, information: str):
        '''
        :param information: text you want to write into file
        '''
        with open(self.file_path, 'a', encoding='utf-8') as f:
            f.write(information)
        print(f'The information has been written into the file "{self.file_path}"')

    def read_text(self):
        '''
        :return: string with an information from the file
        '''
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read()

