import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CanLogComponent } from './can-log.component';

describe('CanLogComponent', () => {
  let component: CanLogComponent;
  let fixture: ComponentFixture<CanLogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CanLogComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CanLogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
