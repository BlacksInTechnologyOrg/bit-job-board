import 'whatwg-fetch'

const BASE = ''
const headers = new Headers({
  'Accept': 'appication/json',
  'Content-Type': 'appication/json'
})

const addToken = () => {
  const token = window.localStorage.getItem('JWT_TOKEN')
  headers.append('Authorization', `JWT ${token}`)
}

export function post (path, body) {
  const init = {
    headers: headers,
    method: 'POST',
    mode: 'cors',
    body: JSON.stringify(body)
  }
  return fetch(BASE + path, init)
}

export function get (path) {
  if (!('Authorization' in headers.keys)) {
    addToken()
  }
  const init = {
    headers: headers,
    method: 'GET',
    mode: 'cors'
  }
  return fetch(BASE + path, init)
}

export function put (path, body) {
  if (!('Authorization' in headers.keys)) {
    addToken()
  }
  const init = {
    headers: headers,
    method: 'PUT',
    mode: 'cors',
    body: JSON.stringify(body)
  }
  return fetch(BASE + path, init)
}

export function remove (path) {
  if (!('Authorization' in headers.keys)) {
    addToken()
  }
  const init = {
    headers: headers,
    method: 'DELETE',
    mode: 'cors'
  }
  return fetch(BASE + path, init)
}
