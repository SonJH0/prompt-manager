import json
import os


DATA_FILE = "prompts.json"


def load_prompts():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            prompts = json.load(file)

        if not isinstance(prompts, list):
            return []

        for prompt in prompts:
            prompt.setdefault("title", "")
            prompt.setdefault("category", "")
            prompt.setdefault("content", "")
            prompt.setdefault("favorite", False)

        return prompts

    except json.JSONDecodeError:
        print("데이터 파일을 읽는 중 오류가 발생했습니다.")
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
    print("7. 프롬프트 삭제")
    print("8. 프롬프트 수정")
    print("0. 종료")


def add_prompt(prompts):
    print("\n===== 프롬프트 추가 =====")

    title = input("제목을 입력하세요: ").strip()
    category = input("카테고리를 입력하세요: ").strip()
    content = input("프롬프트 내용을 입력하세요: ").strip()

    if title == "" or category == "" or content == "":
        print("제목, 카테고리, 내용은 비워둘 수 없습니다.")
        return

    prompt = {
        "title": title,
        "category": category,
        "content": content,
        "favorite": False
    }

    prompts.append(prompt)
    print("프롬프트가 추가되었습니다.")


def list_prompts(prompts):
    print("\n===== 전체 프롬프트 목록 =====")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        favorite_mark = "★ " if prompt.get("favorite", False) else ""
        title = prompt.get("title", "")
        category = prompt.get("category", "")

        print(f"{index}. {favorite_mark}{title} [{category}]")


def view_by_category(prompts):
    print("\n===== 카테고리별 조회 =====")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    category = input("조회할 카테고리를 입력하세요: ").strip().lower()

    found = False

    for index, prompt in enumerate(prompts, start=1):
        prompt_category = prompt.get("category", "").lower()

        if prompt_category == category:
            favorite_mark = "★ " if prompt.get("favorite", False) else ""
            title = prompt.get("title", "")
            original_category = prompt.get("category", "")

            print(f"{index}. {favorite_mark}{title} [{original_category}]")
            found = True

    if not found:
        print("해당 카테고리의 프롬프트가 없습니다.")


def search_prompts(prompts):
    print("\n===== 프롬프트 검색 =====")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    keyword = input("검색어를 입력하세요: ").strip().lower()

    if keyword == "":
        print("검색어를 입력해주세요.")
        return

    found = False

    for index, prompt in enumerate(prompts, start=1):
        title = prompt.get("title", "")
        category = prompt.get("category", "")
        content = prompt.get("content", "")

        if (
            keyword in title.lower()
            or keyword in category.lower()
            or keyword in content.lower()
        ):
            favorite_mark = "★ " if prompt.get("favorite", False) else ""
            print(f"{index}. {favorite_mark}{title} [{category}]")
            found = True

    if not found:
        print("검색 결과가 없습니다.")


def view_prompt_detail(prompts):
    print("\n===== 프롬프트 상세 보기 =====")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    list_prompts(prompts)

    try:
        number = int(input("상세히 볼 프롬프트 번호를 입력하세요: "))

        if number < 1 or number > len(prompts):
            print("잘못된 번호입니다.")
            return

        prompt = prompts[number - 1]

        print("\n===== 프롬프트 상세 정보 =====")
        print(f"제목: {prompt.get('title', '')}")
        print(f"카테고리: {prompt.get('category', '')}")
        print(f"즐겨찾기: {'예' if prompt.get('favorite', False) else '아니오'}")
        print("내용:")
        print(prompt.get("content", ""))

    except ValueError:
        print("숫자를 입력해주세요.")


def manage_favorites(prompts):
    print("\n===== 즐겨찾기 관리 =====")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    list_prompts(prompts)

    try:
        number = int(input("즐겨찾기를 변경할 프롬프트 번호를 입력하세요: "))

        if number < 1 or number > len(prompts):
            print("잘못된 번호입니다.")
            return

        prompt = prompts[number - 1]
        prompt["favorite"] = not prompt.get("favorite", False)

        if prompt["favorite"]:
            print(f"'{prompt.get('title', '')}' 프롬프트가 즐겨찾기에 추가되었습니다.")
        else:
            print(f"'{prompt.get('title', '')}' 프롬프트가 즐겨찾기에서 해제되었습니다.")

    except ValueError:
        print("숫자를 입력해주세요.")


def delete_prompt(prompts):
    print("\n===== 프롬프트 삭제 =====")

    if len(prompts) == 0:
        print("삭제할 프롬프트가 없습니다.")
        return

    list_prompts(prompts)

    try:
        number = int(input("삭제할 프롬프트 번호를 입력하세요: "))

        if number < 1 or number > len(prompts):
            print("잘못된 번호입니다.")
            return

        prompt = prompts[number - 1]

        confirm = input(f"'{prompt.get('title', '')}' 프롬프트를 정말 삭제하시겠습니까? (y/n): ")

        if confirm.lower() != "y":
            print("삭제를 취소했습니다.")
            return

        deleted_prompt = prompts.pop(number - 1)
        print(f"'{deleted_prompt.get('title', '')}' 프롬프트가 삭제되었습니다.")

    except ValueError:
        print("숫자를 입력해주세요.")


def edit_prompt(prompts):
    print("\n===== 프롬프트 수정 =====")

    if len(prompts) == 0:
        print("수정할 프롬프트가 없습니다.")
        return

    list_prompts(prompts)

    try:
        number = int(input("수정할 프롬프트 번호를 입력하세요: "))

        if number < 1 or number > len(prompts):
            print("잘못된 번호입니다.")
            return

        prompt = prompts[number - 1]

        print("\n현재 정보")
        print(f"제목: {prompt.get('title', '')}")
        print(f"카테고리: {prompt.get('category', '')}")
        print(f"내용: {prompt.get('content', '')}")

        print("\n새로운 값을 입력하세요.")
        print("그대로 두려면 Enter만 누르세요.")

        new_title = input("새 제목: ").strip()
        new_category = input("새 카테고리: ").strip()
        new_content = input("새 내용: ").strip()

        if new_title != "":
            prompt["title"] = new_title

        if new_category != "":
            prompt["category"] = new_category

        if new_content != "":
            prompt["content"] = new_content

        print("프롬프트가 수정되었습니다.")

    except ValueError:
        print("숫자를 입력해주세요.")


def main():
    prompts = load_prompts()

    while True:
        show_menu()

        choice = input("메뉴를 선택하세요: ").strip()

        if choice == "1":
            add_prompt(prompts)
            save_prompts(prompts)

        elif choice == "2":
            list_prompts(prompts)

        elif choice == "3":
            view_by_category(prompts)

        elif choice == "4":
            search_prompts(prompts)

        elif choice == "5":
            view_prompt_detail(prompts)

        elif choice == "6":
            manage_favorites(prompts)
            save_prompts(prompts)

        elif choice == "7":
            delete_prompt(prompts)
            save_prompts(prompts)

        elif choice == "8":
            edit_prompt(prompts)
            save_prompts(prompts)

        elif choice == "0":
            save_prompts(prompts)
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()