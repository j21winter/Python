console.log('running...')
const days ={   '0': 'Sunday', 
                '1':'Monday', 
                '2': 'Tuesday', 
                '3': 'Wednesday', 
                '4':'Thursday', 
                '5':'Friday', 
                '6': 'Saturday'
            }

function chooseCity(element){
    var city = element.innerText
    alert(`loading weather report...`)
}
function removeCookie(elementID){
    var cookieMessage = document.getElementById(elementID)
    cookieMessage.remove()
}

function convertToF(temp){
    var conversion = (1.8*temp + 32)
    var newTemp = Math.round(conversion)
    return newTemp
}

function convertToC(temp){
    var conversion = ((temp - 32) /1.8)
    var newTemp = Math.round(conversion)
    return newTemp
}

var tempUnit = '°C'

function changeUnit(choice){
    for(var i = 1 ; i <=9 ; i++){
        var tempElement = document.querySelector('.temp' + i)
        var tempNum = parseInt(tempElement.innerText)
        if(choice.value == '°C'){
            tempUnit = choice
            tempElement.innerText = convertToC(tempNum) + '°'
        } else {
            tempUnit = choice
            tempElement.innerText = convertToF(tempNum) + '°'
        }
    }
}


// API STUFF 

function build_page(data){
    temp_data = get_temp_data(data)

    document.getElementById('city_name').innerText = data['city']['name']
    document.getElementById('current_temp').innerText = data['list'][0]['main']['temp']
    
    temp_count = 1
    day_count = 0
    for(var i = 0; i < 4 ; i++){
        document.getElementById('day_'+day_count).innerText = temp_data['day_'+day_count]['day']
        document.getElementById('temp'+temp_count).innerText = temp_data['day_'+day_count]['max'] +'°'
        temp_count += 1
        document.getElementById('temp'+temp_count).innerText = temp_data['day_'+day_count]['min'] +'°'
        temp_count += 1
        day_count += 1
        document.getElementById(`description_${day_count}`).innerText = temp_data['day_'+day_count]['weather_description']
    }
    if(tempUnit != '°C'){
        changeUnit(tempUnit)
    }


    return data
}

function get_temp_data(data){
    var temp_data = {
                    'day_0':{
                        'day': undefined,
                        'min': undefined,
                        'max': undefined,
                        'weather_description':undefined
                    },
                    'day_1':{
                        'day': undefined,
                        'min': undefined,
                        'max': undefined,
                        'weather_description':undefined
                    },
                    'day_2':{
                        'day': undefined,
                        'min': undefined,
                        'max': undefined,
                        'weather_description':undefined
                    },
                    'day_3':{
                        'day': undefined,
                        'min': undefined,
                        'max': undefined,
                        'weather_description':undefined
                    }
                }

    var date = new Date(data['list'][0]['dt_txt']).toDateString()
    var count = 0
    var min_temp = undefined
    var max_temp = undefined
    
    for(var i = 0; count <= 3; i++){
        var list_date = new Date(data['list'][i]['dt_txt']).toDateString()

        if(list_date == date){
            
            if(temp_data['day_'+count]['day'] == undefined ){
                temp_data['day_'+count]['day'] = days[new Date(list_date).getDay()]
            }
            if(temp_data['day_'+count]['weather_description'] == undefined ){
                temp_data['day_'+count]['weather_description'] = data['list'][i]['weather'][0]['description']
                }

            var temp = data['list'][i]['main']['temp']

            if(min_temp == undefined){
                min_temp = temp
                    }
                else if(temp < min_temp){
                    min_temp = temp
                    }

            if(max_temp == undefined){
                max_temp = temp
                    }
                else if(temp > max_temp){
                    max_temp = temp
                    }
                }

        else{

            temp_data['day_'+count]['min'] = Math.round(min_temp)
            temp_data['day_'+count]['max'] = Math.round(max_temp)
            min_temp = undefined
            max_temp = undefined
            count += 1
            date = list_date
            var temp = data['list'][i]['main']['temp']
            if(min_temp == undefined){
                min_temp = temp
                }
                else if(temp < min_temp){
                    min_temp = temp
                }
            if(max_temp == undefined){
                max_temp = temp
                }
                else if(temp > max_temp){
                    max_temp = temp
                }
        }
    }
        console.log('Temp Data is\n' + temp_data)
        return temp_data
}




const api_key = '&appid=389d82eb77438a06941d120c2ec70127'
const api_url = 'https://api.openweathermap.org/data/2.5/forecast?id='

// Call API OPEN WEATHER
async function open_weather(city_name){
    var city_data = {
        'burbank': '4885983',
        'chicago': '4887398',
        'dallas': '4462896',
    }
    var response = await fetch (api_url + city_data[city_name] + api_key + '&units=metric')
    var city_data = await response.json()

    console.log(city_data['list'][0]['main'])

    return build_page(city_data);
}
// console.log(new Date().toLocaleDateString())
// console.log(new Date().toDateString())
// console.log(new Date('2023-08-26 21:00:00').toDateString())
