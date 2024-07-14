# Python 코드로 BGM 만들어보기!

[text](봉명동.m4a)

- 파일은 playmusic.py 참고

- 'music_scale.txt' => 음계 장표
- 'music1_1_1.txt' => 높은음자리 건반
- 'music1_2_1.txt' => 낮은음자리 건반
- 악보는 포트리스 once_in_a_lifetime 참고

## 코드 해석

- 스레드를 이용한 2 화음 피아노 연주
- 악보를 기준으로 각 음계의 길이와 음정을 파일화 한 데이터를 멀티스레드로 실행
- 파이썬의 코드로는 스레드 딜레이의 한계가 있기 때문에 프로그램의 지원을 받는 것을 추천

```python

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

# text 파일을 불러와 node에 대한 정보를 할당
def load_notes_from_text_file(file_path):
    notes = []
    with open(file_path, 'r') as file:
        for line in file:
            note_info = line.strip().split(',')
            note_tuple = tuple(map(int, note_info))
            notes.append(note_tuple)
    return notes

# notes의 note, velocity, duration 값을 각 하기의 값에 입력
def play_notes(notes, port):
    for note, velocity, duration in notes:
        port.note_on(note, velocity)
        pygame.time.wait(duration)
        port.note_off(note, velocity)

# 메인 함수 실행
def main():
    # 음계 파일 불러오기
    file_path1_1_1 = 'music1_1_1.txt'
    file_path1_2_1 = 'music1_2_1.txt'

    # 각 파일의 값을 변수에 할당
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
```