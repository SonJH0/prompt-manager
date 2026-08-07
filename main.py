def show_menu():
    print("\n===== 프롬프트 관리 프로그램 =====")
    print("1. 프롬프트 추가")
    print("2. 전체 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 상세 보기")
    print("6. 즐겨찾기 관리")
    print("0. 종료")


def main():
    while True:
        show_menu()
        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            print("프롬프트 추가 기능은 준비 중입니다.")
        elif choice == "2":
            print("전체 목록 보기 기능은 준비 중입니다.")
        elif choice == "3":
            print("카테고리별 조회 기능은 준비 중입니다.")
        elif choice == "4":
            print("프롬프트 검색 기능은 준비 중입니다.")
        elif choice == "5":
            print("상세 보기 기능은 준비 중입니다.")
        elif choice == "6":
            print("즐겨찾기 관리 기능은 준비 중입니다.")
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()