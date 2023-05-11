from processor.dataprocessor_service import DataProcessorService


"""
    Main-модуль, т.е. модуль запуска приложений ("точка входа" приложения)
"""


if __name__ == '__main__':
    # Без указания полного пути, программа будет читать файл из своей корневой папки
    DataProcessorService("SYB65_328_202209_Intentional_homicides_and_other_crimes_1.csv").run_service()
