from datetime import datetime
from pylatexenc.latexwalker import LatexWalker, LatexCharsNode

def read_latex_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_sentences_to_file(sentences, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for sentence in sentences:
            file.write(f"{sentence}\n")

def extract_text_nodes(latex_content):
    walker = LatexWalker(latex_content)
    text_nodes = []

    nodes, _, _ = walker.get_latex_nodes(pos=0)

    for node in nodes:
        if node.isNodeType(LatexWalkerNode.NT_CHARS):
            text_nodes.append(node.chars)

    return text_nodes

def main():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    tex_file_path = "C:\\Users\\hejacobsen\\Downloads\\cameras_and_sensors.tex"
    sentences_file_path = f"C:\\Users\\hejacobsen\\OneDrive - AKVA Group\\DEV\\TestingOutput\\Test check\\sentences_{timestamp}.txt"

    
    latex_content = read_latex_file(tex_file_path)
    text_nodes = extract_text_nodes(latex_content)
    
    write_sentences_to_file(text_nodes, sentences_file_path)
    print(f"Sentences extracted to {sentences_file_path}")

if __name__ == "__main__":
    main()
