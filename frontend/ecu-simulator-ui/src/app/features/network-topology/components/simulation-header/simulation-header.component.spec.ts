import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SimulationHeaderComponent } from './simulation-header.component';

describe('SimulationHeaderComponent', () => {
  let component: SimulationHeaderComponent;
  let fixture: ComponentFixture<SimulationHeaderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SimulationHeaderComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SimulationHeaderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
