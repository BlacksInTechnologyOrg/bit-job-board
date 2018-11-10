import axios from 'axios'

const API_URL = 'http://devdesktop.com:8008/api'

export function logInSite (payload) {
  return axios.post(`${API_URL}/auth/login`, payload)
}
export function registerToSite (payload) {
  return axios.post(`${API_URL}/auth/registration`, payload)
}

export function searchContracts (search) {
  return axios.get(`${API_URL}/Contracts/`, {
    params: {
      author: search
    }
  })
}

export function saveSurveyResponse (surveyResponse) {
  return axios.put(`${API_URL}/surveys/${surveyResponse.id}/`, surveyResponse)
}

export function postNewSurvey (survey) {
  return axios.post(`${API_URL}/surveys/`, survey)
}
