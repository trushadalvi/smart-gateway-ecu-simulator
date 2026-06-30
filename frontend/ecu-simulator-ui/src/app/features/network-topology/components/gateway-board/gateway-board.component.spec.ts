import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GatewayBoardComponent } from './gateway-board.component';

describe('GatewayBoardComponent', () => {
  let component: GatewayBoardComponent;
  let fixture: ComponentFixture<GatewayBoardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GatewayBoardComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GatewayBoardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
