window.onload = () => {
    const colorizerPre = document.getElementById('colorizer');
    let children = colorizerPre.children;

    const colorizerTokens = [];
    for (let i = 0; i < children.length; i++) {
        const child = children[i];
        const colorizerContents = {}

        colorizerContents['tokens'] = child.innerText;
        colorizerContents['css'] = {
            color: child.style.color,
            fontWeight: child.style.fontWeight
        }
        colorizerTokens.push(colorizerContents);
    }

    const pygmentsPre = document.getElementById('pygments');
    children = pygmentsPre.children;

    const pygmentsTokens = [];
    for (let i = 0; i < children.length; i++) {
        const child = children[i];
        const pygmentsContents = {};

        pygmentsContents['tokens'] = child.innerText;
        pygmentsContents['css'] = {
            color: child.style.color,
            fontWeight: child.style.fontWeight
        }
        pygmentsTokens.push(pygmentsContents)
    }
    
}