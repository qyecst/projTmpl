module.exports = {
    'env': {
        'browser': true,
        'es6': true
    },
    'extends': 'airbnb-base',
    'globals': {
        'Atomics': 'readonly',
        'SharedArrayBuffer': 'readonly'
    },
    'parserOptions': {
        'ecmaVersion': 2018,
        'sourceType': 'module'
    },
    'rules': {
        // 'indent': ['error', 4, { SwitchCase: 1 }],
        // 'max-len': ['error', 120],
        // 'no-underscore-dangle': 'off',
        // 'object-property-newline': 'off',
        // 'object-curly-newline': 'off',
        // 'no-restricted-syntax': 'off',
        // 'no-param-reassign': 'off',
        // 'no-lonely-if': 'off',
    }
};
