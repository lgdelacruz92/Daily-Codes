window.onload = () => {
    const colorizerPre = document.getElementById('colorizer');
    let children = colorizerPre.children;

    const colorizerTokens = {};
    for (let i = 0; i < children.length; i++) {
        const child = children[i];

        colorizerTokens[child.innerText.trim()] = {
            color: child.style.color,
            fontWeight: child.style.fontWeight
        }
    }

    const pygmentsPre = document.getElementById('pygments');
    children = pygmentsPre.children;

    let str = ''
    const seen = new Set();
    for (let i = 0; i < children.length; i++) {
        const child = children[i];
        const token = child.innerText.trim();
        const className = child.className;
        if (token !== '"' && token in colorizerTokens) {
            if (className == 's')  {
                console.log(className, token, child);
            }
            
            const cssDef = [`.highlight .${className}{\n`,
                    `\tcolor: ${colorizerTokens[token].color};\n`,
            ];
            const fontWeight = colorizerTokens[token].fontWeight;
            if (fontWeight !== '') {
                cssDef.push(`\tfont-weight: ${fontWeight};\n`)
            };
            cssDef.push('}\n')
            const css = cssDef.join('');
            if (!seen.has(cssDef[0].trim())) {
                str += css;
                seen.add(cssDef[0].trim());
            }
        }
    }
    console.log(str);
}