import { createRouter, createWebHistory } from 'vue-router'
import login from '../views/login.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: login
  },{
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/test',
    name: 'test',
    // route level code-splitting
    // this generates a separate chunk (test.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "test" */ '../views/TestView.vue')
  },
  {
    path: '/login',
    name: 'login',
    // route level code-splitting
    // this generates a separate chunk (test.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "login" */ '../views/login.vue')
  },
  {
    path: '/com_register',
    name: 'com_register',
    // route level code-splitting
    // this generates a separate chunk (test.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "com_register" */ '../views/CompanyRegister.vue')
  },
  {
    path: '/stud_register',
    name: 'stud_register',
    // route level code-splitting
    // this generates a separate chunk (test.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "stud_register" */ '../views/StudentRegister.vue')
  },
  {
    path: '/register',
    name: 'register',
    // route level code-splitting
    // this generates a separate chunk (test.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "register" */ '../views/Register.vue')
  },
  {
    path: '/create_drive',
    name: 'create_drive',
    // route level code-splitting
    // this generates a separate chunk (test.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "create_drive" */ '../views/CreateDrive.vue')
  },
  {
    path: '/com_dashboard',
    name: 'com_dashboard',
    // route level code-splitting
    // this generates a separate chunk (test.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "com_dashboard" */ '../views/CompanyDashboard.vue')
  },
  {
    path: '/stud_dashboard',
    name: 'stud_dashboard',
    // route level code-splitting
    // this generates a separate chunk (test.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "stud_dashboard" */ '../views/StudentDashboard.vue')
  },
  {
    path: '/admin_dashboard',
    name: 'admin_dashboard',
    // route level code-splitting
    // this generates a separate chunk (test.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "admin_dashboard" */ '../views/AdminDashboard.vue')
  },
    {
      path: '/drive_details/:id',
      name: 'drive_details',
      // route level code-splitting
      // this generates a separate chunk (test.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "drive_details" */ '../views/DriveDetails.vue')
    },
    {
      path: '/drive_application/:id',
      name: 'drive_application',
      // route level code-splitting
      // this generates a separate chunk (test.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "drive_application" */ '../views/DriveApplication.vue')
    },
    {
      path: '/application_history/:id',
      name: 'application_history',
      // route level code-splitting
      // this generates a separate chunk (test.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "application_history" */ '../views/ApplicationHistory.vue')
    },
    {
      path: '/company_drive/:id',
      name: 'company_drive',
      // route level code-splitting
      // this generates a separate chunk (test.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "company_drive" */ '../views/CompanyDrive.vue')
    },
    {
    path: '/application_details/:id',
    name: 'application_details',
    // route level code-splitting
    // this generates a separate chunk (test.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "application_details" */ '../views/ApplicationDetails.vue')
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
