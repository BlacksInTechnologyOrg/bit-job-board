import axios from 'axios'

const API_URL = 'http://localhost:8008/api'

export function logInSite (payload) {
  console.log('logging in!')
  return axios.post(`${API_URL}/auth/login`, payload)
}

export function fetchSurvey (surveyId) {
  return axios.get(`${API_URL}/surveys/${surveyId}/`)
}

export function saveSurveyResponse (surveyResponse) {
  return axios.put(`${API_URL}/surveys/${surveyResponse.id}/`, surveyResponse)
}

export function postNewSurvey (survey) {
  return axios.post(`${API_URL}/surveys/`, survey)
}
