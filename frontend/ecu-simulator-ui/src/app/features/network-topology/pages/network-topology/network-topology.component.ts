import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

import { SimulationHeaderComponent } from '../../components/simulation-header/simulation-header.component';
import { ControlPanelComponent } from '../../components/control-panel/control-panel.component';
import { GatewayBoardComponent } from '../../components/gateway-board/gateway-board.component';
import { RulesPanelComponent } from '../../components/rules-panel/rules-panel.component';
import { CanLogComponent } from '../../components/can-log/can-log.component';
import { EventTimelineComponent } from '../../components/event-timeline/event-timeline.component';
import { StatusFooterComponent } from '../../components/status-footer/status-footer.component';

@Component({
  selector: 'app-network-topology',
  standalone: true,

  imports: [
    CommonModule,

    SimulationHeaderComponent,
    ControlPanelComponent,
    GatewayBoardComponent,
    RulesPanelComponent,
    CanLogComponent,
    EventTimelineComponent,
    StatusFooterComponent
  ],

  templateUrl: './network-topology.component.html',

  styleUrl: './network-topology.component.scss'
})
export class NetworkTopologyComponent {

}