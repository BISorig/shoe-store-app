export default [
    {
        files: ["app/static/scripts/**/*.js"],
        languageOptions: {
            ecmaVersion: 2022,
            sourceType: "module",
            globals: {
                window: "readonly",
                document: "readonly",
                fetch: "readonly",
                FormData: "readonly",
                URLSearchParams: "readonly",
                console: "readonly",
                location: "readonly",
                confirm: "readonly",
            },
        },
        rules: {
            "no-unused-vars": ["error", { argsIgnorePattern: "^_" }],
            "no-undef": "error",
            semi: ["error", "always"],
            quotes: ["error", "double", { avoidEscape: true }],
        },
    },
];
