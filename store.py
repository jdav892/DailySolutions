    def _prepare_function(self, func, update_globals=None):
        
        wrapped = super(LintSandbox, self)._prepare_function(func, update_globals)
        _, glob = self.unwrap(wrapped)
        builtins = glob["__builtins__"]
        code = func.__code__

        imports_set = set()
        split_imports_set = set()

        for _from, _import, _as in self._imports.get(func, ()):
            if _as:
                imports_set.add(_as)
                split_imports_set.add(_as)
            else:
                what = _import.split(".")[0]
                split_imports_set.add(what)
                imports_set.add(_import)
            if _from == "__builtin__" and _import in builtins:
                e = NameError(f"builtin '{_import}' doesn't need to be imported")
                self._raise_from(e, func)

        paths_map = defaultdict(list)
        for import_name in imports_set:
            parts = import_name.split(".")
            subpaths = [parts[:i] for i in range(1, len(parts) + 1)]
            paths_map[parts[0]].extend(subpaths)
        
        instructions = list(Bytecode(code))
        import_instr_lines = {}
        for instr in instructions:
            if instr.opname in ("IMPORT_NAME", "IMPORT_FROM"):
                import_instr_lines[instr.argval] = instr.starts_line
            if (
                instr.opname == "LOAD_GLOBAL"
                and instr.argval not in glob
                and instr.argval not in split_imports_set
                and instr.argval not in builtins
                and instr.argval not in code.co_varnames[: code.co_argcount]
            ):
                # Raise the same kind of error as what would happen during
                # execution.
                e = NameError(f"global name '{instr.argval}' is not defined")
                if instr.starts_line is None:
                    self._raise_from(e, func)
                else:
                    self._raise_from(e, func, instr.starts_line - code.co_firstlineno)
            
        used_imports = self._find_used_imports(code, paths_map)
        unused_imports = imports_set - used_imports
        if unused_imports:
            import_name = next(iter(unused_imports))
            e = NameError(f"imported name '{import_name}' is not used")
            line = import_instr_lines.get(import_name)
            if line is None:
                self._raise_from(e, func)
            else:
                self._raise_from(e, func, line - code.co_firstlineno)
        return wrapped

    @staticmethod
    def _find_used_imports(code, paths_map):
        used = set()
        instructions = list(Bytecode(code))
        for idx, instr in enumerate(instructions):
            if instr.opname == "LOAD_GLOBAL" and instr.argval in paths_map:
                paths_tracked = [instr.argval]
                for follow in instructions[idx + 1:]:
                    if follow.opname == "LOAD_ATTR":
                        paths_tracked.append(follow.argval)
                    else:
                        break
            
                for candidate_path in paths_map[paths_tracked[0]]:
                    if candidate_path[: len(paths_tracked)] == paths_tracked:
                        used.add(".".join(candidate_path))
                        break


        for const in code.co_consts:
            if isinstance(const, types.CodeType):
                used |= LintSandbox._find_used_imports(const, paths_map)
        
        return used
    
    
    
        def test_unnecessary_imports(self):
        with self.assertRaisesFromLine(NameError, 3) as e:
            with self.moz_configure(
                """
                option(env='FOO', help='Foo')
                @depends('FOO')
                @imports("os")
                def foo(value):
                    return value
            """
            ):
                self.lint_test()

        self.assertEqual(str(e.exception), "imported name 'os' is not used")

        with self.assertRaisesFromLine(NameError, 3) as e:
            with self.moz_configure(
                """
                option(env='FOO', help='Foo')
                @depends('FOO')
                @imports("os.path")
                def foo(value):
                    return value
            """
            ):
                self.lint_test()
                assert False, "lint_test did not raise"
        self.assertEqual(str(e.exception), "imported name 'os.path' is not used")

        with self.assertRaisesFromLine(NameError, 3) as e:
            with self.moz_configure(
                """
                option(env='FOO', help='Foo')
                @depends('FOO')
                @imports(_from="os.path", _import="isdir")
                def foo(value):
                    return value
            """
            ):
                self.lint_test()

        self.assertEqual(str(e.exception), "imported name 'isdir' is not used")

        with self.assertRaisesFromLine(NameError, 3) as e:
            with self.moz_configure(
                """
                option(env='FOO', help='Foo')
                @depends('FOO')
                @imports(_from="collections", _import="deque")
                def foo(value):
                    return value
            """
            ):
                self.lint_test()

        self.assertEqual(str(e.exception), "imported name 'deque' is not used")

        with self.assertRaisesFromLine(NameError, 3) as e:
            with self.moz_configure(
                """
                option(env='FOO', help='Foo')
                @depends('FOO')
                @imports(_from="selenium", _import="driver")
                def foo(value):
                    return value
            """
            ): 
                self.lint_test()
        
        self.assertEqual(str(e.exception), "imported name 'driver' is not used")
 

        with self.assertRaisesFromLine(NameError, 3) as e:
            with self.moz_configure(
                """
                option(env='FOO', help='Foo')
                @depends('FOO')
                @imports(_from="collections", _import="Counter")
                def foo(value):
                    return value
            """
            ): 
                self.lint_test()
       
        self.assertEqual(str(e.exception), "imported name 'Counter' is not used")
 
        with self.assertRaisesFromLine(NameError, 3) as e:
            with self.moz_configure(
                """
                option(env='FOO', help='Foo')
                @depends('FOO')
                @imports(_from="flask", _import="Flask")
                def foo(value):
                    return value
            """
            ): 
                self.lint_test()
       
        self.assertEqual(str(e.exception), "imported name 'Flask' is not used")
 


        with self.assertRaisesFromLine(NameError, 3) as e:
            with self.moz_configure(
                """
                option(env='FOO', help='Foo')
                @depends('FOO')
                @imports(_from="os.path", _import="join", _as="path_join")
                def foo(value):
                    return value
            """
            ):
                self.lint_test()

        self.assertEqual(str(e.exception), "imported name 'path_join' is not used")

       
#        try:
#            with self.moz_configure(
#                """
#                option(env='FOO', help='Foo')
#                @depends('FOO')
#                @imports("os")
#                def foo(value):
#                    def inner(path):
#                        return os.path.join(path, "bar")
#                    return inner(value)
#            """
#            ):
#                self.lint_test()
#        except NameError as e:
#            if "os" in str(e) and "not used" in str(e):
#                self.fail(f"Unexpected linter error on: {e} as unused when used inside a nested function")
#            else:
#                False

## --->Anything from here down is what I came up with, above is LLM assisted

def _prepare_function(self, func, update_globals=None):
        wrapped = super(LintSandbox, self)._prepare_function(func, update_globals)
        _, glob = self.unwrap(wrapped)
        builtins = glob["__builtins__"]
        imports = set()
        split_imports = set()
        for _from, _import, _as in self._imports.get(func, ()):
            if _as:
                imports.add(_as)
                split_imports.add(_as)
            else:
                what = _import.split(".")[0]
                imports.add(_import)
                split_imports.add(what)
            if _from == "__builtin__" and _import in builtins:
                print(imports)
                print(split_imports)
                e = NameError(f"builtin '{_import}' doesn't need to be imported")
                self._raise_from(e, func)
        for instr in Bytecode(func):
            code = func.__code__
            if (
                instr.opname == "LOAD_GLOBAL"
                and instr.argval not in glob
                and instr.argval not in imports
                and instr.argval not in builtins
                and instr.argval not in code.co_varnames[: code.co_argcount]
            ):
                # Raise the same kind of error as what would happen during
                # execution.
                e = NameError(f"global name '{instr.argval}' is not defined")
                if instr.starts_line is None:
                    self._raise_from(e, func)
                else:
                    self._raise_from(e, func, instr.starts_line - code.co_firstlineno)

        return wrapped
    
    
    
     def test_unnecessary_imports(self):
        with self.assertRaisesFromLine(NameError, 3) as e:
            with self.moz_configure(
                """
                option(env='FOO', help='Foo')
                @depends('FOO')
                @imports(_from='__builtin__', _import='list')
                def foo(value):
                    if value:
                        return list()
                    return value
            """
            ):
                self.lint_test()

        self.assertEqual(str(e.exception), "builtin 'list' doesn't need to be imported")
        
        with self.assertRaisesFromLine(NameError, 3) as e:
            with self.moz_configure(
                """
                option(env='FOO', help='Foo')
                @depends('FOO')
                @imports(_from='collections', _import='Counter')
                def foo(value):
                    return value
            """
            ):
                self.lint_test()
        self.assertEqual(str(e.exception), "import 'Counter' is not used")

        try:
            with self.moz_configure(
                """
                option(env='FOO', help='Foo')
                @depends('FOO')
                @imports("os")
                def foo(value):
                    def inner(path):
                        return os.path.join(path, "bar")
                    return inner(value)
            """
            ):
                self.lint_test()
        except NameError as e: 
            if "os" in str(e) and "not used" in str(e): 
                self.fail(f"Unexpected error on {e}")
            else: 
                False

