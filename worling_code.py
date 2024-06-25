import cv2
import numpy as np

def create_text_video():
    #Текст в видео
    text_message = input("Введите текст, который хотите видеть в видео: ")
    #Частота кадров
    fps = int(input("Введите частоту кадров (FPS видео): "))
    #Длительность видео
    time = int(input("Введите продолжительность видео: "))
    #Длина и ширина
    width, height = 100, 100
    out = cv2.VideoWriter("text_video_opencv.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    #Кадр с черным фоном
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    #Начальные координаты для бегущей строки
    x, y = width, height // 2
    #Параметры шрифта
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1
    font_thickness = 2
    font_color = (255, 255, 255)  # Белый цвет текста
    #Само видео
    for t in range(time*fps):  #время умножить на частоту равно общему количеству кадров и итераций
        # Очистка предыдущего кадра, чтобы не мешал новому
        frame.fill(0)
        x -= 1+2*(width*(len(text_message)+1)//((time)*fps*7)) #сдвиг за кадр равен пути, который нужно пройти делить на количество кадров
        #Собественно текст
        cv2.putText(frame, text_message, (x, y), font, font_scale, font_color, font_thickness)
        #Записать кадр в видео
        out.write(frame)
    #Закончить видео после окончания цикла
    out.release()
#Вызываем функцию
create_text_video()   
    
        
        
        
        
    
    
    
    