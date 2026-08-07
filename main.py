def show_menu():
    print("\n===== 프롬프트 관리 프로그램 =====")
    print("1. 프롬프트 추가")
    print("2. 전체 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 상세 보기")
    print("6. 즐겨찾기 관리")
    print("0. 종료")


def add_prompt(prompts):
    title = input("제목을 입력하세요: ")
    category = input("카테고리를 입력하세요: ")
    content = input("프롬프트 내용을 입력하세요: ")

    prompt = {
        "title": title,
        "category": category,
        "content": content,
        "favorite": False
    }

    prompts.append(prompt)
    print("프롬프트가 추가되었습니다.")


def list_prompts(prompts):
    if len(prompts) == 0:
        print("저장된 프롬프트가 없습니다.")
        return

    print("\n===== 전체 프롬프트 목록 =====")

    for index, prompt in enumerate(prompts, start=1):
        print(f"{index}. {prompt['title']} [{prompt['category']}]")


def list_by_category(prompts):
    if len(prompts) == 0:
        print("저장된 프롬프트가 없습니다.")
        return

    category = input("조회할 카테고리를 입력하세요: ")

    filtered_prompts = []

    for prompt in prompts:
        if prompt["category"] == category:
            filtered_prompts.append(prompt)

    if len(filtered_prompts) == 0:
        print("해당 카테고리의 프롬프트가 없습니다.")
        return

    print(f"\n===== {category} 카테고리 목록 =====")

    for index, prompt in enumerate(filtered_prompts, start=1):
        print(f"{index}. {prompt['title']} [{prompt['category']}]")


def search_prompts(prompts):
    if len(prompts) == 0:
        print("저장된 프롬프트가 없습니다.")
        return

    keyword = input("검색어를 입력하세요: ")

    search_results = []

    for prompt in prompts:
        title = prompt["title"]
        category = prompt["category"]
        content = prompt["content"]

        if keyword in title or keyword in category or keyword in content:
            search_results.append(prompt)

    if len(search_results) == 0:
        print("검색 결과가 없습니다.")
        return

    print(f"\n===== '{keyword}' 검색 결과 =====")

    for index, prompt in enumerate(search_results, start=1):
        print(f"{index}. {prompt['title']} [{prompt['category']}]")


def show_prompt_detail(prompts):
    if len(prompts) == 0:
        print("저장된 프롬프트가 없습니다.")
        return

    print("\n===== 상세 보기할 프롬프트 선택 =====")

    for index, prompt in enumerate(prompts, start=1):
        print(f"{index}. {prompt['title']} [{prompt['category']}]")

    selected = input("상세 보기할 번호를 입력하세요: ")

    if not selected.isdigit():
        print("숫자를 입력해주세요.")
        return

    selected_index = int(selected) - 1

    if selected_index < 0 or selected_index >= len(prompts):
        print("존재하지 않는 번호입니다.")
        return

    prompt = prompts[selected_index]

    print("\n===== 프롬프트 상세 정보 =====")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"내용: {prompt['content']}")

    if prompt["favorite"]:
        print("즐겨찾기: 등록됨")
    else:
        print("즐겨찾기: 등록 안 됨")


def main():
    prompts = []

    while True:
        show_menu()
        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            add_prompt(prompts)

        elif choice == "2":
            list_prompts(prompts)

        elif choice == "3":
            list_by_category(prompts)

        elif choice == "4":
            search_prompts(prompts)

        elif choice == "5":
            show_prompt_detail(prompts)

        elif choice == "6":
            print("즐겨찾기 관리 기능은 준비 중입니다.")

        elif choice == "0":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()