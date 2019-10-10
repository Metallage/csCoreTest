# -*- coding: UTF-8 -*-

import sys
import subprocess #импорт модуля запуска сторонних программ
import argparse #импорт модуля работы с аргументами

#текст для преобразования
testText = 'AS as'
#контрольный текст
controlText = 'AS\tas'
#команда на вызов тестируемого проекта
cmd = ["dotnet", "run", "--project"]


#парсим аргументы
def CreateParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--project', required=True)
    parser.add_argument('-t', '--testfile', required=True)
    return parser

#пишем в тестовый файл текст для преобразования
def WriteToFile(filePath, text):
    testFile = open(filePath,"w")
    testFile.write(text)

#считываем из преобразованного файла текст и сверяем с эталоном
def ControlRead(filePath, controlText):
    controlFile = open(filePath, "r")
    tmpText = controlFile.read()
    print(tmpText)
    print(controlText)
    return tmpText == controlText


if __name__ == "__main__":

    parser = CreateParser()
    namespace = parser.parse_args(sys.argv[1:])
    testFilePath = namespace.testfile
    pathToProject = namespace.project
    
    WriteToFile(testFilePath , testText)
    cmd +=[pathToProject, testFilePath]
    process = subprocess.Popen(cmd)
    process.wait()

    testPassed = ControlRead(testFilePath, controlText)
    print(testPassed)
