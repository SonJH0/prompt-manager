import json
import os


FILE_NAME = "prompts.json"


def get_default_prompts():
    """기본 프롬프트 데이터"""
    return [
        {
            "title": "블로그 글 작성",
            "category": "글쓰기",
            "content": "주제에 맞는 블로그 글을 작성해주세요.",
            "favorite": False,
            "views": 0
        },
        {
            "title": "이메일 작성",
            "category": "업무",
            "content": "상황에 맞는 정중한 이메일을 작성해주세요.",
            "favorite": False,
            "views": 0
        },
        {
            "title": "파이썬 코드 설명",
            "category": "코딩",
            "content": "다음 파이썬 코드를 초보자도 이해할 수 있게 설명해주세요.",
            "favorite": False,
            "views": 0
        }
    ]


def ensure_prompt_fields(prompts):
    """기존 데이터에 필요한 필드가 없으면 기본값 추가"""
    for prompt in prompts:
        if "favorite" not in prompt:
            prompt["favorite"] = False

        if "views" not in prompt:
            prompt["views"] = 0


def load_prompts():
    """프롬프트 데이터를 파일에서 불러오기"""
    if not os.path.exists(FILE_NAME):
        prompts = get_default_prompts()
        save_prompts(prompts)
        return prompts

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            prompts = json.load(file)

        ensure_prompt_fields(prompts)
        return prompts

    except json.JSONDecodeError:
        print("prompts.json 파일을 읽는 중 오류가 발생했습니다.")
        print("기본 프롬프트로 시작합니다.")
        return get_default_prompts()


def save_prompts(prompts):
    """프롬프트 데이터를 파일에 저장하기"""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=4)


def show_menu():
    """메인 메뉴 출력"""
    print("\n===== 프롬프트 관리 프로그램 =====")
    print("1. 프롬프트 추가")
    print("2. 전체 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록 보기")
    print("8. 프롬프트 수정")
    print("9. 프롬프트 삭제")
    print("10. 조회수 TOP 목록 보기")
    print("0. 종료")


def add_prompt(prompts):
    """프롬프트 추가 기능"""
    print("\n===== 프롬프트 추가 =====")

    title = input("제목을 입력하세요: ")
    category = input("카테고리를 입력하세요: ")
    content = input("프롬프트 내용을 입력하세요: ")

    if not title.strip() or not category.strip() or not content.strip():
        print("제목, 카테고리, 내용은 비워둘 수 없습니다.")
        return

    prompt = {
        "title": title,
        "category": category,
        "content": content,
        "favorite": False,
        "views": 0
    }

    prompts.append(prompt)
    print("프롬프트가 추가되었습니다.")


def show_all_prompts(prompts):
    """전체 프롬프트 목록 보기"""
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    print("\n===== 전체 프롬프트 목록 =====")

    for i, prompt in enumerate(prompts, start=1):
        favorite_mark = "★" if prompt.get("favorite", False) else "☆"
        views = prompt.get("views", 0)

        print(
            f"{i}. {favorite_mark} {prompt['title']} "
            f"[{prompt['category']}] - 조회수 {views}회"
        )


def show_by_category(prompts):
    """카테고리별 프롬프트 조회"""
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    category = input("조회할 카테고리를 입력하세요: ")

    filtered_prompts = []

    for prompt in prompts:
        if prompt["category"] == category:
            filtered_prompts.append(prompt)

    if len(filtered_prompts) == 0:
        print(f"'{category}' 카테고리의 프롬프트가 없습니다.")
        return

    print(f"\n===== {category} 카테고리 목록 =====")

    for i, prompt in enumerate(filtered_prompts, start=1):
        favorite_mark = "★" if prompt.get("favorite", False) else "☆"
        views = prompt.get("views", 0)

        print(
            f"{i}. {favorite_mark} {prompt['title']} "
            f"[{prompt['category']}] - 조회수 {views}회"
        )


def search_prompts(prompts):
    """프롬프트 검색 기능"""
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    keyword = input("검색어를 입력하세요: ")

    search_results = []

    for prompt in prompts:
        if (
            keyword.lower() in prompt["title"].lower()
            or keyword.lower() in prompt["category"].lower()
            or keyword.lower() in prompt["content"].lower()
        ):
            search_results.append(prompt)

    if len(search_results) == 0:
        print(f"'{keyword}' 검색 결과가 없습니다.")
        return

    print(f"\n===== '{keyword}' 검색 결과 =====")

    for i, prompt in enumerate(search_results, start=1):
        favorite_mark = "★" if prompt.get("favorite", False) else "☆"
        views = prompt.get("views", 0)

        print(
            f"{i}. {favorite_mark} {prompt['title']} "
            f"[{prompt['category']}] - 조회수 {views}회"
        )


def show_prompt_detail(prompts):
    """프롬프트 상세 보기 기능 + 조회수 증가"""
    if not prompts:
        print("상세 보기할 프롬프트가 없습니다.")
        return

    print("\n===== 프롬프트 상세 보기 =====")

    for i, prompt in enumerate(prompts, start=1):
        favorite_mark = "★" if prompt.get("favorite", False) else "☆"
        print(f"{i}. {favorite_mark} {prompt['title']} [{prompt['category']}]")

    try:
        number = int(input("상세 보기할 프롬프트 번호를 입력하세요: "))

        if number < 1 or number > len(prompts):
            print("잘못된 번호입니다.")
            return

        prompt = prompts[number - 1]

        # 상세 보기를 할 때마다 조회수 1 증가
        prompt["views"] = prompt.get("views", 0) + 1

        favorite_mark = "★" if prompt.get("favorite", False) else "☆"

        print("\n===== 프롬프트 상세 정보 =====")
        print(f"제목: {prompt['title']}")
        print(f"카테고리: {prompt['category']}")
        print(f"즐겨찾기: {favorite_mark}")
        print(f"조회수: {prompt['views']}회")
        print(f"내용: {prompt['content']}")

    except ValueError:
        print("숫자를 입력해주세요.")


def manage_favorites(prompts):
    """즐겨찾기 등록/해제 기능"""
    if not prompts:
        print("즐겨찾기를 관리할 프롬프트가 없습니다.")
        return

    while True:
        print("\n===== 즐겨찾기 관리 =====")
        print("1. 즐겨찾기 등록/해제")
        print("2. 즐겨찾기 목록 보기")
        print("0. 이전 메뉴로 돌아가기")

        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            print("\n===== 즐겨찾기 등록/해제 =====")

            for i, prompt in enumerate(prompts, start=1):
                favorite_mark = "★" if prompt.get("favorite", False) else "☆"
                print(f"{i}. {favorite_mark} {prompt['title']} [{prompt['category']}]")

            try:
                number = int(input("즐겨찾기를 변경할 번호를 입력하세요: "))

                if number < 1 or number > len(prompts):
                    print("잘못된 번호입니다.")
                    continue

                prompt = prompts[number - 1]
                prompt["favorite"] = not prompt.get("favorite", False)

                if prompt["favorite"]:
                    print(f"'{prompt['title']}' 프롬프트가 즐겨찾기에 등록되었습니다.")
                else:
                    print(f"'{prompt['title']}' 프롬프트가 즐겨찾기에서 해제되었습니다.")

                save_prompts(prompts)

            except ValueError:
                print("숫자를 입력해주세요.")

        elif choice == "2":
            show_favorite_prompts(prompts)

        elif choice == "0":
            break

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


def show_favorite_prompts(prompts):
    """즐겨찾기 목록만 보기"""
    favorite_prompts = []

    for prompt in prompts:
        if prompt.get("favorite", False):
            favorite_prompts.append(prompt)

    if len(favorite_prompts) == 0:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    print("\n===== 즐겨찾기 목록 =====")

    for i, prompt in enumerate(favorite_prompts, start=1):
        views = prompt.get("views", 0)
        print(
            f"{i}. ★ {prompt['title']} "
            f"[{prompt['category']}] - 조회수 {views}회"
        )


def edit_prompt(prompts):
    """프롬프트 수정 기능"""
    if not prompts:
        print("수정할 프롬프트가 없습니다.")
        return

    print("\n===== 프롬프트 수정 =====")

    for i, prompt in enumerate(prompts, start=1):
        print(f"{i}. {prompt['title']} [{prompt['category']}]")

    try:
        number = int(input("수정할 프롬프트 번호를 입력하세요: "))

        if number < 1 or number > len(prompts):
            print("잘못된 번호입니다.")
            return

        prompt = prompts[number - 1]

        print("\n수정하지 않을 항목은 Enter만 누르세요.")

        new_title = input(f"새 제목 ({prompt['title']}): ")
        new_category = input(f"새 카테고리 ({prompt['category']}): ")
        new_content = input(f"새 내용 ({prompt['content']}): ")

        if new_title.strip():
            prompt["title"] = new_title

        if new_category.strip():
            prompt["category"] = new_category

        if new_content.strip():
            prompt["content"] = new_content

        print("프롬프트가 수정되었습니다.")

    except ValueError:
        print("숫자를 입력해주세요.")


def delete_prompt(prompts):
    """프롬프트 삭제 기능"""
    if not prompts:
        print("삭제할 프롬프트가 없습니다.")
        return

    print("\n===== 프롬프트 삭제 =====")

    for i, prompt in enumerate(prompts, start=1):
        print(f"{i}. {prompt['title']} [{prompt['category']}]")

    try:
        number = int(input("삭제할 프롬프트 번호를 입력하세요: "))

        if number < 1 or number > len(prompts):
            print("잘못된 번호입니다.")
            return

        prompt = prompts[number - 1]

        confirm = input(f"'{prompt['title']}' 프롬프트를 정말 삭제할까요? (y/n): ")

        if confirm.lower() == "y":
            deleted_prompt = prompts.pop(number - 1)
            print(f"'{deleted_prompt['title']}' 프롬프트가 삭제되었습니다.")
        else:
            print("삭제를 취소했습니다.")

    except ValueError:
        print("숫자를 입력해주세요.")


def show_top_viewed_prompts(prompts):
    """조회수 기준 TOP 목록 보기"""
    if not prompts:
        print("조회수 목록을 볼 프롬프트가 없습니다.")
        return

    sorted_prompts = sorted(
        prompts,
        key=lambda prompt: prompt.get("views", 0),
        reverse=True
    )

    print("\n===== 조회수 TOP 목록 =====")

    for i, prompt in enumerate(sorted_prompts, start=1):
        favorite_mark = "★" if prompt.get("favorite", False) else "☆"
        views = prompt.get("views", 0)

        print(
            f"{i}. {favorite_mark} {prompt['title']} "
            f"[{prompt['category']}] - 조회수 {views}회"
        )


def main():
    """프로그램 메인 실행 함수"""
    prompts = load_prompts()
    ensure_prompt_fields(prompts)

    while True:
        show_menu()

        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            add_prompt(prompts)
            save_prompts(prompts)

        elif choice == "2":
            show_all_prompts(prompts)

        elif choice == "3":
            show_by_category(prompts)

        elif choice == "4":
            search_prompts(prompts)

        elif choice == "5":
            show_prompt_detail(prompts)
            save_prompts(prompts)

        elif choice == "6":
            manage_favorites(prompts)
            save_prompts(prompts)

        elif choice == "7":
            show_favorite_prompts(prompts)

        elif choice == "8":
            edit_prompt(prompts)
            save_prompts(prompts)

        elif choice == "9":
            delete_prompt(prompts)
            save_prompts(prompts)

        elif choice == "10":
            show_top_viewed_prompts(prompts)

        elif choice == "0":
            save_prompts(prompts)
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()