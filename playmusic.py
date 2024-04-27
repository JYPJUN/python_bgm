import pygame
import pygame.midi
import threading

# Pygame 및 MIDI 초기화
pygame.init()
pygame.mixer.init()
pygame.midi.init()

# MIDI 포트 열기 및 설정
port = pygame.midi.Output(0)
port.set_instrument(0)

def load_notes_from_text_file(file_path):
    notes = []
    with open(file_path, 'r') as file:
        for line in file:
            note_info = line.strip().split(',')
            note_tuple = tuple(map(int, note_info))
            notes.append(note_tuple)
    return notes

def play_notes(notes, port):
    for note, velocity, duration in notes:
        port.note_on(note, velocity)
        pygame.time.wait(duration)
        port.note_off(note, velocity)

def main():
    # 음계 파일 불러오기
    file_path1_1_1 = 'music1_1_1.txt'
    file_path1_2_1 = 'music1_2_1.txt'

    notes1_1_1 = load_notes_from_text_file(file_path1_1_1)
    notes1_2_1 = load_notes_from_text_file(file_path1_2_1)

    # 스레드 생성 및 실행
    thread1_1_1 = threading.Thread(target=play_notes, args=(notes1_1_1, port))
    thread1_2_1 = threading.Thread(target=play_notes, args=(notes1_2_1, port))

    thread1_1_1.start()
    thread1_2_1.start()

    thread1_1_1.join()
    thread1_2_1.join()

if __name__ == "__main__":
    try:
        # while True:
            main()
    finally:
        # 모든 리소스 정리
        del port
        pygame.midi.quit()
        pygame.quit()