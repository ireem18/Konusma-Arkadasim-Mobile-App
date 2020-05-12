import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { OfferpagePage } from './offerpage.page';

describe('OfferpagePage', () => {
  let component: OfferpagePage;
  let fixture: ComponentFixture<OfferpagePage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OfferpagePage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(OfferpagePage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
