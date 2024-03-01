import openai
import subprocess


def prepare_documentation(code_snippet):
    system_content = """
        Your task is to assist in generating documentation for code from a repository. 
        Based on the code provided, you need to return documentation that is ready for publication on GitHub Pages. 
        You will only use the provided code using the provided data and nothing else."""

    user_query = f"""
        Code snippet:
        ---
        {code_snippet}
        --- 
        Provide a documentation for this code suitable for GitHub Pages"""
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": system_content},
                  {"role": "user", "content": user_query}],
        temperature=0.7,
        top_p=1
    )
    print(response)
    return response.choices[0].message.content


def get_changed_files():
    result = subprocess.run(['git', 'rev-parse', '--verify', 'HEAD~1'], stderr=subprocess.PIPE)
    if result.returncode != 0:
        result = subprocess.run(['git', 'ls-files'], stdout=subprocess.PIPE)
    else:
        result = subprocess.run(['git', 'diff', '--name-only', 'HEAD~1'], stdout=subprocess.PIPE)
    changed_files = result.stdout.decode('utf-8').splitlines()
    return changed_files


def read_code_from_files(file_list):
    code_snippet = ""
    for file in file_list:
        if file.endswith(".py"):
            with open(file, 'r') as f:
                code_snippet += f.read() + "\n\n"
    return code_snippet


changed_files = get_changed_files()
code_snippet = read_code_from_files(changed_files)
documentation = prepare_documentation(code_snippet)

with open('docs/index.md', 'w') as file:
    file.write(documentation)

