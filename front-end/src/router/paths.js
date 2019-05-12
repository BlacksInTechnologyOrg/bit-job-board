/**
 * Define all of your application routes here
 * for more information on routes, see the
 * official documentation https://router.vuejs.org/en/
 */
export default [
  {
    path: '/',
    view: 'Home'
  },
  {
    path: '/login',
    view: 'Login'
  },
  {
    path: '/register',
    view: 'Register'
  },
  {
    path: '/search',
    name: 'Search',
    view: 'SearchListing'
  },
  {
    path: '/jobs/:jobid',
    view: 'Job'
  },
  {
    path: '/contracts/:contractid',
    view: 'Contract'
  },
  {
    path: '/dashboard',
    // Relative to /src/views
    view: 'Dashboard',
    meta: {
      dashboard: true
    }
  },
  {
    path: '/dashboard/contract/create',
    // Relative to /src/views
    view: 'ContractCreation',
    meta: {
      dashboard: true
    }
  },
  {
    path: '/user-profile',
    name: 'User Profile',
    view: 'UserProfile',
    meta: {
      dashboard: true
    }

  },
  {
    path: '/table-list',
    name: 'Table List',
    view: 'TableList',
    meta: {
      dashboard: true
    }

  },
  {
    path: '/typography',
    view: 'Typography',
    meta: {
      dashboard: true
    }

  },
  {
    path: '/icons',
    view: 'Icons',
    meta: {
      dashboard: true
    }

  },
  {
    path: '/maps',
    view: 'Maps',
    meta: {
      dashboard: true
    }

  },
  {
    path: '/notifications',
    view: 'Notifications',
    meta: {
      dashboard: true
    }

  },
  {
    path: '/upgrade',
    name: 'Upgrade to PRO',
    view: 'Upgrade',
    meta: {
      dashboard: true
    }
  }
]
