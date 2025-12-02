import socket


def check_chrome_port(host="127.0.0.1", port=9222):
    """
    주어진 포트(9222)가 열려있는지 확인하여
    Chrome 원격 디버깅 모드가 실행 중인지 진단합니다.
    """
    print("-" * 50)
    print(f"🕵️  진단 시작: {host}:{port} 포트의 문을 두드려봅니다...")

    # 1. 소켓 생성 및 타임아웃 설정 (3초)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    # 2. 연결 시도 후 결과 확인
    result = sock.connect_ex((host, port))

    # 3. 결과에 따른 진단 메시지 출력
    if result == 0:
        print("\n✅✅✅ [성공] 연결 가능! ✅✅✅")
        print("Chrome 브라우저가 원격 조종 모드로 실행 중이며, 연결을 기다리고 있습니다.")
        print("만약 Selenium 에러가 계속된다면, Chrome과 Chromedriver의 버전 호환성 문제일 수 있습니다.")
    else:
        print("\n❌❌❌ [실패] 연결 불가! ❌❌❌")
        print("이것이 에러의 원인입니다. Chrome이 9222번 포트를 열어두지 않았습니다.")
        print("\n🤔 아래 항목을 다시 확인해보세요:")
        print("  1. 모든 Chrome 창을 '완전히' 종료했나요?")
        print("  2. 터미널에서 '원격 조종 모드' 명령어를 정확히 실행했나요?")
        print("  3. 명령어를 실행한 터미널 창과 새로 열린 Chrome 창을 끄지 않고 그대로 두었나요?")

    sock.close()
    print("-" * 50)


# --- 진단 도구 실행 ---
if __name__ == "__main__":
    check_chrome_port()