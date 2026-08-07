import json
import os

DATA_FILE = "prompts.json"


def load_prompts():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            prompts = json.load(file)

            for prompt in prompts:
                if "favorite" not in prompt:
                    prompt["favorite"] = False

            return prompts

    except json.JSONDecodeError:
        print("데이터 파일을 읽는 중 오류가 발생했습니다. 빈 목록으로 시작합니다.")
        return []


def save_prompts(prompts):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=4)


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
        star = "★" if prompt["favorite"] else "☆"
        print(f"{index}. {star} {prompt['title']} [{prompt['category']}]")


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
        star = "★" if prompt["favorite"] else "☆"
        print(f"{index}. {star} {prompt['title']} [{prompt['category']}]")


def search_prompts(prompts):
    if len(prompts) == 0:
        print("저장된 프롬프트가 없습니다.")
        return

    keyword = input("검색어를 입력하세요: ")

    results = []

    for prompt in prompts:
        if (
            keyword.lower() in prompt["title"].lower()
            or keyword.lower() in prompt["category"].lower()
            or keyword.lower() in prompt["content"].lower()
        ):
            results.append(prompt)

    if len(results) == 0:
        print("검색 결과가 없습니다.")
        return

    print("\n===== 검색 결과 =====")

    for index, prompt in enumerate(results, start=1):
        star = "★" if prompt["favorite"] else "☆"
        print(f"{index}. {star} {prompt['title']} [{prompt['category']}]")


def show_detail(prompts):
    if len(prompts) == 0:
        print("저장된 프롬프트가 없습니다.")
        return

    list_prompts(prompts)

    try:
        number = int(input("상세 보기할 번호를 입력하세요: "))

        if number < 1 or number > len(prompts):
            print("잘못된 번호입니다.")
            return

        prompt = prompts[number - 1]

        print("\n===== 프롬프트 상세 정보 =====")
        print(f"제목: {prompt['title']}")
        print(f"카테고리: {prompt['category']}")
        print(f"즐겨찾기: {'등록됨' if prompt['favorite'] else '등록 안 됨'}")
        print(f"내용: {prompt['content']}")

    except ValueError:
        print("숫자를 입력해주세요.")


def toggle_favorite(prompts):
    if len(prompts) == 0:
        print("저장된 프롬프트가 없습니다.")
        return

    print("\n===== 즐겨찾기 등록/해제 =====")

    for index, prompt in enumerate(prompts, start=1):
        star = "★" if prompt["favorite"] else "☆"
        print(f"{index}. {star}{prompt['title']} [{prompt['category']}]")

    try:
        number = int(input("즐겨찾기를 변경할 번호를 입력하세요: "))

        if number < 1 or number > len(prompts):
            print("잘못된 번호입니다.")
            return

        prompt = prompts[number - 1]
        prompt["favorite"] = not prompt["favorite"]

        if prompt["favorite"]:
            print(f"'{prompt['title']}' 프롬프트가 즐겨찾기에 등록되었습니다.")
        else:
            print(f"'{prompt['title']}' 프롬프트가 즐겨찾기에서 해제되었습니다.")

    except ValueError:
        print("숫자를 입력해주세요.")


def list_favorites(prompts):
    favorites = []

    for prompt in prompts:
        if prompt["favorite"]:
            favorites.append(prompt)

    if len(favorites) == 0:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    print("\n===== 즐겨찾기 목록 =====")

    for index, prompt in enumerate(favorites, start=1):
        print(f"{index}. ★ {prompt['title']} [{prompt['category']}]")


def manage_favorites(prompts):
    while True:
        print("\n===== 즐겨찾기 관리 =====")
        print("1. 즐겨찾기 등록/해제")
        print("2. 즐겨찾기 목록 보기")
        print("0. 이전 메뉴로 돌아가기")

        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            toggle_favorite(prompts)
            save_prompts(prompts)

        elif choice == "2":
            list_favorites(prompts)

        elif choice == "0":
            break

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


def main():
    prompts = load_prompts()

    while True:
        show_menu()
        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            add_prompt(prompts)
            save_prompts(prompts)

        elif choice == "2":
            list_prompts(prompts)

        elif choice == "3":
            list_by_category(prompts)

        elif choice == "4":
            search_prompts(prompts)

        elif choice == "5":
            show_detail(prompts)

        elif choice == "6":
            manage_favorites(prompts)
            save_prompts(prompts)

        elif choice == "0":
            save_prompts(prompts)
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()