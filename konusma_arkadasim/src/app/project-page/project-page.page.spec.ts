import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { ProjectPagePage } from './project-page.page';

describe('ProjectPagePage', () => {
  let component: ProjectPagePage;
  let fixture: ComponentFixture<ProjectPagePage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProjectPagePage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(ProjectPagePage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
