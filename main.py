CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


DEFAULT_PROMPTS = [
    {
        "title": "블로그 글 작성 프롬프트",
        "content": "주제를 입력하면 제목, 소제목, 본문, 마무리 문장으로 구성된 블로그 글을 작성해줘.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "이미지 생성 프롬프트",
        "content": "원하는 장면을 입력하면 분위기, 배경, 조명, 스타일을 포함한 이미지 생성 프롬프트를 작성해줘.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "고객 페르소나 설계 프롬프트",
        "content": "서비스나 제품 정보를 바탕으로 고객의 나이, 직업, 관심사, 문제점, 구매 동기를 포함한 페르소나를 만들어줘.",
        "category": "페르소나",
        "favorite": False
    }
]


def get_initial_prompts():
    prompts = []

    for prompt in DEFAULT_PROMPTS:
        prompts.append(prompt.copy())

    return prompts


def show_menu():
    print("\n===== 프롬프트 관리 프로그램 =====")
    print("1. 프롬프트 추가")
    print("2. 전체 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록 보기")
    print("0. 종료")


def show_categories():
    print("\n===== 카테고리 목록 =====")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")


def choose_category():
    while True:
        show_categories()

        choice = input("카테고리 번호를 선택하거나 직접 입력하세요: ").strip()

        if choice == "":
            print("카테고리는 비워둘 수 없습니다.")
            continue

        if choice.isdigit():
            index = int(choice) - 1

            if 0 <= index < len(CATEGORIES):
                return CATEGORIES[index]
            else:
                print("잘못된 카테고리 번호입니다. 다시 입력해주세요.")
        else:
            return choice


def input_not_empty(message):
    while True:
        value = input(message).strip()

        if value != "":
            return value

        print("입력값은 비워둘 수 없습니다. 다시 입력해주세요.")


def add_prompt(prompts):
    print("\n===== 프롬프트 추가 =====")

    title = input_not_empty("제목을 입력하세요: ")
    content = input_not_empty("내용을 입력하세요: ")
    category = choose_category()

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)

    print("프롬프트가 추가되었습니다.")


def show_list(prompts):
    print("\n===== 전체 프롬프트 목록 =====")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        favorite_mark = "O" if prompt["favorite"] else "X"
        print(f"{index}. {prompt['title']} [{prompt['category']}] 즐겨찾기: {favorite_mark}")


def show_by_category(prompts):
    print("\n===== 카테고리별 조회 =====")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    category = choose_category()

    print(f"\n===== [{category}] 카테고리 프롬프트 =====")

    found = False

    for index, prompt in enumerate(prompts, start=1):
        if prompt["category"] == category:
            favorite_mark = "O" if prompt["favorite"] else "X"
            print(f"{index}. {prompt['title']} 즐겨찾기: {favorite_mark}")
            found = True

    if not found:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")


def search_prompt(prompts):
    print("\n===== 프롬프트 검색 =====")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    keyword = input_not_empty("검색어를 입력하세요: ")

    print(f"\n===== '{keyword}' 검색 결과 =====")

    found = False

    for index, prompt in enumerate(prompts, start=1):
        title = prompt["title"]
        content = prompt["content"]

        if keyword.lower() in title.lower() or keyword.lower() in content.lower():
            favorite_mark = "O" if prompt["favorite"] else "X"
            print(f"{index}. {prompt['title']} [{prompt['category']}] 즐겨찾기: {favorite_mark}")
            found = True

    if not found:
        print("검색 결과가 없습니다.")


def show_detail(prompts):
    print("\n===== 프롬프트 상세 보기 =====")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list(prompts)

    number = input("상세 보기할 프롬프트 번호를 입력하세요: ").strip()

    if not number.isdigit():
        print("숫자를 입력해주세요.")
        return

    index = int(number) - 1

    if index < 0 or index >= len(prompts):
        print("잘못된 번호입니다.")
        return

    prompt = prompts[index]
    favorite_mark = "O" if prompt["favorite"] else "X"

    print("\n===== 프롬프트 상세 정보 =====")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {favorite_mark}")
    print("내용:")
    print(prompt["content"])


def manage_favorite(prompts):
    print("\n===== 즐겨찾기 관리 =====")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list(prompts)

    number = input("즐겨찾기를 추가/해제할 프롬프트 번호를 입력하세요: ").strip()

    if not number.isdigit():
        print("숫자를 입력해주세요.")
        return

    index = int(number) - 1

    if index < 0 or index >= len(prompts):
        print("잘못된 번호입니다.")
        return

    prompts[index]["favorite"] = not prompts[index]["favorite"]

    if prompts[index]["favorite"]:
        print("즐겨찾기에 추가되었습니다.")
    else:
        print("즐겨찾기에서 해제되었습니다.")


def show_favorites(prompts):
    print("\n===== 즐겨찾기 목록 =====")

    favorite_count = 0

    for index, prompt in enumerate(prompts, start=1):
        if prompt["favorite"]:
            print(f"{index}. {prompt['title']} [{prompt['category']}]")
            favorite_count += 1

    if favorite_count == 0:
        print("즐겨찾기된 프롬프트가 없습니다.")


def main():
    prompts = get_initial_prompts()

    while True:
        show_menu()

        choice = input("메뉴를 선택하세요: ").strip()

        if choice == "1":
            add_prompt(prompts)

        elif choice == "2":
            show_list(prompts)

        elif choice == "3":
            show_by_category(prompts)

        elif choice == "4":
            search_prompt(prompts)

        elif choice == "5":
            show_detail(prompts)

        elif choice == "6":
            manage_favorite(prompts)

        elif choice == "7":
            show_favorites(prompts)

        elif choice == "0":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()