import shlex

cleaned_lines = []

print("the github: https://github.com/I-like-linux/Dodecal")

file_run = input("> ")

if file_run.endswith(".dodecal") or file_run.endswith(".dc.dev"):

    try:
        with open(file_run, "r") as file:
            code = file.read()

        lines = code.splitlines()

        # Preprocess lines
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#"):
                continue

            # Handle ^string^ syntax
            if line.count("^") >= 2:
                first = line.find("^")
                last = line.rfind("^")
                inner = line[first+1:last]
                line = line[:first] + "\"" + inner + "\"" + line[last+1:]

            cleaned_lines.append(line)

        # Tokenize
        tokenized_prgm = []
        for line in cleaned_lines:
            tokens = shlex.split(line)
            tokenized_prgm.append(tokens)

        variables = {}

        def get_value(token):
            # String literal
            if (token.startswith("'") and token.endswith("'")) or (token.startswith('"') and token.endswith('"')):
                return token[1:-1]

            # Integer
            if token.isdigit():
                return int(token)

            # Variable
            if token in variables:
                return variables[token]

            return token

        # Label indexing
        labels = {}
        for i, tokens in enumerate(tokenized_prgm):
            if tokens[0] == "label":
                labels[tokens[1]] = i

        ip = 0

        # MAIN EXECUTION LOOP
        while ip < len(tokenized_prgm):
            tokens = tokenized_prgm[ip]
            cmd = tokens[0]

            # BASIC OPS
            if cmd == "add":
                variables[tokens[3]] = get_value(tokens[1]) + get_value(tokens[2])
                ip += 1

            elif cmd == "sub":
                variables[tokens[3]] = get_value(tokens[1]) - get_value(tokens[2])
                ip += 1

            elif cmd == "mul":
                variables[tokens[3]] = get_value(tokens[1]) * get_value(tokens[2])
                ip += 1

            elif cmd == "div":
                variables[tokens[3]] = get_value(tokens[1]) / get_value(tokens[2])
                ip += 1

            elif cmd == "set":
                variables[tokens[1]] = get_value(tokens[2])
                ip += 1

            # PRINTING (variable-aware)
            elif cmd == "print":
                out = " ".join(tokens[1:])
                if out in variables:
                    print(variables[out])
                else:
                    print(out.strip('"'))
                ip += 1

            elif cmd == "printn":
                out = " ".join(tokens[1:])
                if out in variables:
                    print(variables[out], end="")
                else:
                    print(out.strip('"'), end="")
                ip += 1

            # INPUT
            elif cmd == "input":
                prompt = " ".join(tokens[2:]).strip('"')
                variables[tokens[1]] = input(prompt)
                ip += 1

            # LABELS
            elif cmd == "label":
                ip += 1

            elif cmd == "goto":
                ip = labels[tokens[1]]

            elif cmd == "if":
                left = get_value(tokens[1])
                op = tokens[2]
                right = get_value(tokens[3])

                # Evaluate condition (numeric if possible)
                cond = False
                try:
                    lf = float(left)
                    rf = float(right)
                    if op == "<":
                        cond = lf < rf
                    elif op == ">":
                        cond = lf > rf
                    elif op == "<=":
                        cond = lf <= rf
                    elif op == ">=":
                        cond = lf >= rf
                    elif op == "==":
                        cond = left == right
                    elif op == "!=":
                        cond = left != right
                except:
                    # fallback to string compare
                    if op == "==":
                        cond = left == right
                    elif op == "!=":
                        cond = left != right

                #INLINE IF DETECTION
                if len(tokens) > 4:
                    if cond:
                        inline_cmd = tokens[4]
                        args = tokens[5:]

                        if inline_cmd == "print":
                            out = " ".join(args)
                            if out in variables:
                                print(variables[out])
                            else:
                                print(out.strip('"'))

                        elif inline_cmd == "printn":
                            out = " ".join(args)
                            if out in variables:
                                print(variables[out], end="")
                            else:
                                print(out.strip('"'), end="")

                        elif inline_cmd == "set":
                            variables[args[0]] = get_value(args[1])

                        elif inline_cmd == "add":
                            variables[args[2]] = get_value(args[0]) + get_value(args[1])

                        elif inline_cmd == "sub":
                            variables[args[2]] = get_value(args[0]) - get_value(args[1])

                        elif inline_cmd == "mul":
                            variables[args[2]] = get_value(args[0]) * get_value(args[1])

                        elif inline_cmd == "div":
                            variables[args[2]] = get_value(args[0]) / get_value(args[1])

                        elif inline_cmd == "goto":
                            ip = labels[args[0]]
                            continue

                    ip += 1
                    continue

                if cond:
                    ip += 1
                else:
                    depth = 1
                    ip += 1
                    while ip < len(tokenized_prgm) and depth > 0:
                        if tokenized_prgm[ip][0] == "if":
                            depth += 1
                        elif tokenized_prgm[ip][0] == "endif":
                            depth -= 1
                        ip += 1

            elif cmd == "endif":
                ip += 1

            else:
                ip += 1

    except FileNotFoundError:
        print("E: No Valid Dodecal File Found")
        exit()

else:
    print("E: No Valid Dodecal File Found")
    exit()
