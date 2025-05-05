import json
import sys

def fill_values(values_file_path, tests_file_path, report_file_path):

    with open(values_file_path, 'r') as f:
        values_data = json.load(f)

    with open(tests_file_path, 'r') as f:
        tests_data = json.load(f)

    def fill_values_recursive(node):
        if isinstance(node, dict):
            if 'id' in node:
                test_id = str(node['id'])
                for item in values_data.get('values', []):  
                    if str(item.get('id')) == test_id:  
                        node['value'] = item.get('value') 
                        break
            for key, value in node.items():
                fill_values_recursive(value)
        elif isinstance(node, list):
            for item in node:
                fill_values_recursive(item)

    fill_values_recursive(tests_data)

    with open(report_file_path, 'w') as f:
        json.dump(tests_data, f, indent=2)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python task3.py values.json tests.json report.json")
        sys.exit(1)

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    try:
        fill_values(values_file, tests_file, report_file)
        print(f"Отчет успешно создан в {report_file}")
    except FileNotFoundError as e:
        print(f"Error: File not found: {e.filename}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)