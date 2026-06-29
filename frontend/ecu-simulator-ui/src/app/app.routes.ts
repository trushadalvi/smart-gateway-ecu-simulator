import { Routes } from '@angular/router';

import { LandingComponent } from './features/landing/pages/landing/landing.component';

import { LoginComponent } from './features/auth/login/pages/login/login.component';
import { SignupComponent } from './features/auth/signup/pages/signup/signup.component';

import { DashboardComponent } from './features/dashboard/pages/dashboard/dashboard.component';

import { ControlCenterComponent } from './features/control-center/pages/control-center/control-center.component';

import { CanMonitorComponent } from './features/can-monitor/pages/can-monitor/can-monitor.component';

import { NetworkTopologyComponent } from './features/network-topology/pages/network-topology/network-topology.component';

import { GatewayRulesComponent } from './features/gateway-rules/pages/gateway-rules/gateway-rules.component';

import { AnalyticsComponent } from './features/analytics/pages/analytics/analytics.component';

import { SettingsComponent } from './features/settings/pages/settings/settings.component';

export const routes: Routes = [
  {
    path: '',
    component: LandingComponent
  },

  {
    path: 'login',
    component: LoginComponent
  },

  {
    path: 'signup',
    component: SignupComponent
  },

  {
    path: 'dashboard',
    component: DashboardComponent
  },

  {
    path: 'control-center',
    component: ControlCenterComponent
  },

  {
    path: 'can-monitor',
    component: CanMonitorComponent
  },

  {
    path: 'network-topology',
    component: NetworkTopologyComponent
  },

  {
    path: 'gateway-rules',
    component: GatewayRulesComponent
  },

  {
    path: 'analytics',
    component: AnalyticsComponent
  },

  {
    path: 'settings',
    component: SettingsComponent
  },

  {
    path: '**',
    redirectTo: ''
  }
];