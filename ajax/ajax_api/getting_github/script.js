function display_user(data){
    if (data.name == null){
        return
    } else {
        const div = document.createElement('div')
        const para = document.createElement('p')
        const img = document.createElement('img')
        document.body.append(div)
        div.append(para, img)
        para.innerText = `${data.name} has ${data.followers} followers `
        img.src = `${data.avatar_url}`
        return data
    }
}

async function getCoderData(username) {
    // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    var response = await fetch(`https://api.github.com/users/${username}`);
    // We then need to convert the data into JSON format.
    var coderData = await response.json();

    display_user(coderData)
    return coderData;
}

document.getElementById('button').onclick = function(){
    const inputValue = document.getElementById('search').value
    console.log(inputValue)
    if (inputValue.length < 1) {
        console.log('inputValue empty!')
        return
    }
    else{
        getCoderData(inputValue)
    
}   
}
