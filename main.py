import json
import os


FILE_NAME = "prompts.json"


def load_prompts():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            prompts = json.load(file)

            if isinstance(prompts, list):
                return prompts
            else:
                return []

    except json.JSONDecodeError:
        return []


def save_prompts(prompts):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=4)


def show_menu():
    print("\n===== 프롬프트 관리 프로그램 =====")
    print("1. 프롬프트 추가")
    print("2. 전체 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 프롬프트 삭제")
    print("8. 프롬프트 수정")
    print("9. 즐겨찾기 목록 보기")
    print("0. 종료")


def add_prompt(prompts):
    print("\n===== 프롬프트 추가 =====")

    title = input("제목: ").strip()
    category = input("카테고리: ").strip()
    content = input("프롬프트 내용: ").strip()

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
        title = prompt.get("title", "제목 없음")
        category = prompt.get("category", "카테고리 없음")
        favorite = prompt.get("favorite", False)

        star = "★" if favorite else "☆"

        print(f"{index}. {star} {title} [{category}]")


def list_by_category(prompts):
    print("\n===== 카테고리별 조회 =====")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    category_input = input("조회할 카테고리: ").strip()

    if category_input == "":
        print("카테고리를 입력해주세요.")
        return

    found = False

    for index, prompt in enumerate(prompts, start=1):
        category = prompt.get("category", "")

        if category == category_input:
            title = prompt.get("title", "제목 없음")
            favorite = prompt.get("favorite", False)
            star = "★" if favorite else "☆"

            print(f"{index}. {star} {title} [{category}]")
            found = True

    if not found:
        print("해당 카테고리의 프롬프트가 없습니다.")


def search_prompts(prompts):
    print("\n===== 프롬프트 검색 =====")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    keyword = input("검색어: ").strip().lower()

    if keyword == "":
        print("검색어를 입력해주세요.")
        return

    found = False

    for index, prompt in enumerate(prompts, start=1):
        title = prompt.get("title", "")
        category = prompt.get("category", "")
        content = prompt.get("content", "")

        search_text = f"{title} {category} {content}".lower()

        if keyword in search_text:
            favorite = prompt.get("favorite", False)
            star = "★" if favorite else "☆"

            print(f"{index}. {star} {title} [{category}]")
            found = True

    if not found:
        print("검색 결과가 없습니다.")


def view_prompt_detail(prompts):
    print("\n===== 프롬프트 상세 보기 =====")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    list_prompts(prompts)

    number = input("상세 보기할 번호: ").strip()

    if not number.isdigit():
        print("숫자를 입력해주세요.")
        return

    index = int(number) - 1

    if index < 0 or index >= len(prompts):
        print("잘못된 번호입니다.")
        return

    prompt = prompts[index]

    title = prompt.get("title", "제목 없음")
    category = prompt.get("category", "카테고리 없음")
    content = prompt.get("content", "")
    favorite = prompt.get("favorite", False)

    star = "★" if favorite else "☆"

    print("\n===== 상세 정보 =====")
    print(f"번호: {index + 1}")
    print(f"즐겨찾기: {star}")
    print(f"제목: {title}")
    print(f"카테고리: {category}")
    print(f"내용: {content}")


def manage_favorite(prompts):
    print("\n===== 즐겨찾기 관리 =====")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    list_prompts(prompts)

    number = input("즐겨찾기를 변경할 번호: ").strip()

    if not number.isdigit():
        print("숫자를 입력해주세요.")
        return

    index = int(number) - 1

    if index < 0 or index >= len(prompts):
        print("잘못된 번호입니다.")
        return

    current = prompts[index].get("favorite", False)
    prompts[index]["favorite"] = not current

    if prompts[index]["favorite"]:
        print("즐겨찾기에 추가되었습니다.")
    else:
        print("즐겨찾기에서 제거되었습니다.")


def delete_prompt(prompts):
    print("\n===== 프롬프트 삭제 =====")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    list_prompts(prompts)

    number = input("삭제할 번호: ").strip()

    if not number.isdigit():
        print("숫자를 입력해주세요.")
        return

    index = int(number) - 1

    if index < 0 or index >= len(prompts):
        print("잘못된 번호입니다.")
        return

    title = prompts[index].get("title", "제목 없음")

    confirm = input(f"'{title}' 프롬프트를 정말 삭제할까요? (y/n): ").strip().lower()

    if confirm == "y":
        deleted_prompt = prompts.pop(index)
        deleted_title = deleted_prompt.get("title", "제목 없음")
        print(f"'{deleted_title}' 프롬프트가 삭제되었습니다.")
    else:
        print("삭제를 취소했습니다.")


def edit_prompt(prompts):
    print("\n===== 프롬프트 수정 =====")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    list_prompts(prompts)

    number = input("수정할 번호: ").strip()

    if not number.isdigit():
        print("숫자를 입력해주세요.")
        return

    index = int(number) - 1

    if index < 0 or index >= len(prompts):
        print("잘못된 번호입니다.")
        return

    prompt = prompts[index]

    old_title = prompt.get("title", "")
    old_category = prompt.get("category", "")
    old_content = prompt.get("content", "")

    print("\n수정하지 않을 항목은 그냥 Enter를 누르세요.")

    new_title = input(f"새 제목 [{old_title}]: ").strip()
    new_category = input(f"새 카테고리 [{old_category}]: ").strip()
    new_content = input(f"새 내용 [{old_content}]: ").strip()

    if new_title != "":
        prompt["title"] = new_title

    if new_category != "":
        prompt["category"] = new_category

    if new_content != "":
        prompt["content"] = new_content

    print("프롬프트가 수정되었습니다.")


def list_favorite_prompts(prompts):
    print("\n===== 즐겨찾기 목록 =====")

    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    favorite_count = 0

    for index, prompt in enumerate(prompts, start=1):
        if prompt.get("favorite", False):
            title = prompt.get("title", "제목 없음")
            category = prompt.get("category", "카테고리 없음")

            print(f"{index}. ★ {title} [{category}]")
            favorite_count += 1

    if favorite_count == 0:
        print("즐겨찾기한 프롬프트가 없습니다.")


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
            list_by_category(prompts)

        elif choice == "4":
            search_prompts(prompts)

        elif choice == "5":
            view_prompt_detail(prompts)

        elif choice == "6":
            manage_favorite(prompts)
            save_prompts(prompts)

        elif choice == "7":
            delete_prompt(prompts)
            save_prompts(prompts)

        elif choice == "8":
            edit_prompt(prompts)
            save_prompts(prompts)

        elif choice == "9":
            list_favorite_prompts(prompts)

        elif choice == "0":
            save_prompts(prompts)
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()