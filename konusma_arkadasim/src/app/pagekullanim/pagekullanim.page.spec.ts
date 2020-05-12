import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { PagekullanimPage } from './pagekullanim.page';

describe('PagekullanimPage', () => {
  let component: PagekullanimPage;
  let fixture: ComponentFixture<PagekullanimPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PagekullanimPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(PagekullanimPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
